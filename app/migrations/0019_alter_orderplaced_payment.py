# Generated by Django 4.1.3 on 2023-01-12 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_orderplaced_ordered_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='payment',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.payment'),
        ),
    ]
