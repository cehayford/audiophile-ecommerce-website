# Generated by Django 4.2.3 on 2023-07-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audiophile_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='Shipping',
            field=models.BooleanField(default=False),
        ),
    ]
