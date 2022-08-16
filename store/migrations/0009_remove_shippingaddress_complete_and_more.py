# Generated by Django 4.0.6 on 2022-07-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_remove_shippingaddress_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='transaction_id',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='complete',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='transaction_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]