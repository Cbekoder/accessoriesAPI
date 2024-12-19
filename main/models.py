from django.db import models, transaction
from django.db.models import Sum
from rest_framework.exceptions import ValidationError

from inventory.models import Product


class InputList(models.Model):
    total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Input list"
        verbose_name_plural = "Input lists"
        ordering = ['-created_at']

    # def save(self, *args, **kwargs):
    #     with transaction.atomic():
    #         if not self.pk:
    #             self.total = self.inputlistitem_set.aggregate(total=Sum('total_sum'))['total'] or 0.0
    #         super().save(*args, **kwargs)

class InputListItem(models.Model):
    input_list = models.ForeignKey(InputList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    arrival_price = models.FloatField()
    sell_price = models.FloatField()
    amount = models.PositiveIntegerField()
    total_sum = models.FloatField()

    class Meta:
        verbose_name = "Input list item"
        verbose_name_plural = "Input list items"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            self.total_sum = self.amount * self.arrival_price
            super().save(*args, **kwargs)
            if self.product.sell_price != self.sell_price:
                self.product.sell_price = self.sell_price
            if self.product.arrival_price != self.arrival_price:
                self.product.arrival_price = self.arrival_price
            self.product.amount += self.amount
            self.product.save()
            self.input_list.total = self.input_list.inputlistitem_set.aggregate(total_sum=Sum('total_sum'))['total_sum'] or 0.0
            self.input_list.save()

    def delete(self, *args, **kwargs):
        with transaction.atomic():
            self.product.amount -= self.amount
            self.product.save()
            super(InputListItem, self).delete(*args, **kwargs)


class Output(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    reason = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.pk is None:
                if self.product.amount < self.amount:
                    raise ValueError("Insufficient stock for the product.")
                self.product.amount -= self.amount
                self.product.save()
            super().save(*args, **kwargs)


class SalesList(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_sum = models.FloatField()

    class Meta:
        ordering = ['-created_at']


class SaleItem(models.Model):
    sales_list = models.ForeignKey(SalesList, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=False)
    amount = models.PositiveIntegerField()
    sell_price = models.FloatField()
    total_sum = models.FloatField()

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.product:
                if self.product.amount < self.amount:
                    raise ValidationError({"error":"Insufficient stock for the product."})
                self.product.amount -= self.amount
                self.product.save()

            self.total_sum = self.amount * self.sell_price
            super().save(*args, **kwargs)

            self.sales_list.total_sum = self.sales_list.saleitem_set.aggregate(total_sum=Sum('total_sum'))['total_sum'] or 0.0
            self.sales_list.save()