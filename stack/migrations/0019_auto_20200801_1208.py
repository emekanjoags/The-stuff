# Generated by Django 2.2.1 on 2020-08-01 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0018_bonusbutton_givebonus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bonusbutton',
            name='action',
        ),
        migrations.AddField(
            model_name='bonusbutton',
            name='active',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
