# Generated by Django 3.1.1 on 2020-12-28 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_jobsapply'),
    ]

    operations = [
        migrations.DeleteModel(
            name='JobsApply',
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='jcompanyname',
            new_name='job_companyname',
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='jexperience',
            new_name='job_experience',
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='jlocation',
            new_name='job_location',
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='jno',
            new_name='job_no',
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='jnotificationdate',
            new_name='job_notificationdate',
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='jsal',
            new_name='job_sal',
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='jtitle',
            new_name='job_title',
        ),
    ]