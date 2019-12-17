from django.contrib import admin
from .models import (
    Project,
    Phone_No,
    Email,
    Account
    )
# Register your models here.
admin.site.register(Project)
admin.site.register(Phone_No)
admin.site.register(Email)
admin.site.register(Account)