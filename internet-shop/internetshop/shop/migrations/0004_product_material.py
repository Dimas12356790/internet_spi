# Generated by Django 5.0.6 on 2024-07-02 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
