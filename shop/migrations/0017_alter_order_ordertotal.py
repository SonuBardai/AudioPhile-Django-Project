# Generated by Django 3.2.9 on 2022-04-06 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderTotal',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
