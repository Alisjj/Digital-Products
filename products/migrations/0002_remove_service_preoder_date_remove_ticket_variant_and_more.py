# Generated by Django 4.0.1 on 2022-02-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='preoder_date',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='variant',
        ),
        migrations.AddField(
            model_name='course',
            name='preorder_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]