# Generated by Django 4.2.1 on 2023-05-24 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahallak', '0003_offer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='location',
        ),
        migrations.AddField(
            model_name='store',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='store'),
        ),
    ]
