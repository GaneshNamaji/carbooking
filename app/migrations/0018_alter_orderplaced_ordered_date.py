# Generated by Django 4.1.3 on 2023-01-12 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_cart_cust'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]