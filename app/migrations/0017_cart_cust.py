# Generated by Django 4.1.3 on 2023-01-12 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_cart_cust'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cust',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.customer'),
        ),
    ]
