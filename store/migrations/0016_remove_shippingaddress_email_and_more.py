# Generated by Django 4.0.6 on 2022-07-29 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_shippingaddress_email_shippingaddress_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='email',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='name',
        ),
    ]
