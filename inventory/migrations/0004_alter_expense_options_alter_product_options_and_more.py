# Generated by Django 5.1.4 on 2024-12-27 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_expense_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-created_at'], 'verbose_name': 'Xarajat ', 'verbose_name_plural': 'Xarajatlar '},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id'], 'verbose_name': 'Mahsulot ', 'verbose_name_plural': 'Mahsulotlar '},
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
