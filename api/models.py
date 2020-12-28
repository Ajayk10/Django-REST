from django.db import models

class Jobs(models.Model):
    job_no = models.IntegerField(null=True)
    job_title = models.CharField(max_length=64,null=True)
    job_companyname = models.CharField(max_length=64,null=True)
    job_sal = models.FloatField(null=True)
    job_experience = models.CharField(max_length=64,null=True)
    job_location = models.CharField(max_length=64,null=True)
    job_notificationdate = models.DateTimeField(auto_now_add=True)

