# Generated by Django 4.2.1 on 2023-05-27 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahallak', '0004_remove_customer_location_store_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='', max_length=500),
        ),
    ]