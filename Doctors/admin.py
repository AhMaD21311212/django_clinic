from django.contrib import admin
from .models import Doctor,Department,Cantact
# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','Department','image')


admin.site.register(Department)
admin.site.register(Cantact)