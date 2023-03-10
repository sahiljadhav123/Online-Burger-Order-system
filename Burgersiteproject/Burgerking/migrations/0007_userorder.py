# Generated by Django 4.1.2 on 2022-12-14 06:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Burgerking', '0006_reply_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('order', models.TextField()),
                ('time_of_order', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'User Order List',
                'verbose_name_plural': 'User Order List',
            },
        ),
    ]
