# Generated by Django 4.1.1 on 2022-09-17 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zazinmori_server', '0002_alter_user_passwd'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='User_info',
        ),
    ]
