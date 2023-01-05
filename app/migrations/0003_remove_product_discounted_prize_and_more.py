# Generated by Django 4.1.3 on 2023-01-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discounted_prize',
        ),
        migrations.RemoveField(
            model_name='product',
            name='prodapp',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('MZ', 'maruti suzuki'), ('HY', 'hyunda'), ('AD', 'audi'), ('JR', 'jaguar'), ('JP', 'jeep'), ('BM', 'bmw'), ('MS', 'mercedes'), ('SK', 'skoda'), ('VO', 'volvo'), ('HO', 'honda'), ('LM', 'lamborghini'), ('PE', 'porsche')], max_length=2),
        ),
    ]
