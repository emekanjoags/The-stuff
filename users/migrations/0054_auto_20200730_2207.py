# Generated by Django 2.2.1 on 2020-07-30 21:07

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0053_auto_20200730_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='uploads/profile/no-img.png', upload_to=utilities.helper.Helper.user_upload_file_name),
        ),
    ]
