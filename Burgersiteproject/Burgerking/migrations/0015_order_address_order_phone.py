# Generated by Django 4.1.2 on 2022-12-21 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Burgerking', '0014_order_delete_details_delete_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
