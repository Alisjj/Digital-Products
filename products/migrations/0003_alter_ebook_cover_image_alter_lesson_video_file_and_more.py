# Generated by Django 4.0.1 on 2022-02-04 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_ebook_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
