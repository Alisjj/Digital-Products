# Generated by Django 4.0.1 on 2022-02-05 21:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_delete_userprofile_alter_user_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='facebook_url',
            field=models.URLField(default=' ', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='profile_link',
            field=models.URLField(default=' ', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default=' ', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='referral_url',
            field=models.URLField(default=' ', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='twitter_url',
            field=models.URLField(default=' ', max_length=150),
            preserve_default=False,
        ),
    ]