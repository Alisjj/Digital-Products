# Generated by Django 4.0.2 on 2022-04-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pricing_tier',
            field=models.ManyToManyField(blank=True, to='subscription.CustomPricing'),
        ),
    ]
