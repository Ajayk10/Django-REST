# Generated by Django 3.1.1 on 2020-12-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_delete_jobs_apply'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobsApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('japply', models.CharField(max_length=64, null=True)),
            ],
        ),
    ]
