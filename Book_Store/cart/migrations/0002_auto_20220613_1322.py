# Generated by Django 3.2.13 on 2022-06-13 07:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
