# Generated by Django 4.0.2 on 2022-05-15 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_cover_imageupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product'),
        ),
    ]