# Generated by Django 4.1.2 on 2022-12-18 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Burgerking', '0008_alter_userorder_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserOrder',
        ),
    ]
