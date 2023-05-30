# Generated by Django 4.2.1 on 2023-05-29 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mahallak', '0006_alter_order_customer_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='offer', to='mahallak.product'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
