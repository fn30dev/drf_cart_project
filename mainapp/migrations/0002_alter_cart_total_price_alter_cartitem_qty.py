# Generated by Django 4.0.5 on 2022-06-28 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='qty',
            field=models.IntegerField(default=0),
        ),
    ]