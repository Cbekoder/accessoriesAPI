# Generated by Django 5.1.4 on 2024-12-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputlistitem',
            name='arrival_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inputlistitem',
            name='sell_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
