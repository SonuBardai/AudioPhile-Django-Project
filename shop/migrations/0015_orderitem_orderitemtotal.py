# Generated by Django 3.2.9 on 2022-04-06 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_remove_orderitem_orderitemtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='orderItemTotal',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
