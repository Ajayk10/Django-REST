# Generated by Django 3.1.1 on 2020-12-24 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201211_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='eno',
            new_name='enos',
        ),
    ]