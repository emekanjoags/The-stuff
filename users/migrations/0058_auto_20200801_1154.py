# Generated by Django 2.2.1 on 2020-08-01 10:55

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0057_auto_20200731_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='uploads/profile/no-img.png', upload_to=utilities.helper.Helper.user_upload_file_name),
        ),
    ]
