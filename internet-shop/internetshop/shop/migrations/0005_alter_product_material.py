# Generated by Django 5.0.6 on 2024-07-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.TextField(blank=True, null=True),
        ),
    ]
