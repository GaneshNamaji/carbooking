# Generated by Django 4.1.3 on 2023-01-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]