# Generated by Django 4.0.1 on 2022-02-07 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_lesson_user_remove_lessondetail_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessondetail',
            name='course',
        ),
        migrations.RemoveField(
            model_name='lessondetail',
            name='name',
        ),
        migrations.AddField(
            model_name='lessondetail',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lessondetail',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.uploadfile'),
        ),
        migrations.AddField(
            model_name='lessondetail',
            name='file_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='lessondetail',
            name='lesson',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.lesson'),
            preserve_default=False,
        ),
    ]
