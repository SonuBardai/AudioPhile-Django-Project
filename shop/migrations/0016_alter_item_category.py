# Generated by Django 3.2.9 on 2022-04-06 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_orderitem_orderitemtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('headphones', 'Headphones'), ('speakers', 'Speakers'), ('earphones', 'Earphones'), ('microphones', 'Microphones')], max_length=100),
        ),
    ]