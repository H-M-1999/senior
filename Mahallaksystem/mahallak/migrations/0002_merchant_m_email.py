# Generated by Django 4.2.1 on 2023-05-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahallak', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='m_email',
            field=models.EmailField(default=' ', max_length=254),
        ),
    ]