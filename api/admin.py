from django.contrib import admin
from .models import *

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ['id','job_no','job_title','job_experience','job_sal',
                    'job_location','job_companyname','job_notificationdate'
                    ]

admin.site.register(Jobs)



