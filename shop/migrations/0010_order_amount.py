# Generated by Django 3.2.9 on 2022-04-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_shippingaddress_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]