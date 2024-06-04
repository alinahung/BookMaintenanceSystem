from django.contrib import admin

# Register your models here.
from accounts.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=("studentId", "register_year", "phone_number", "gender", "birth_date")
    list_filter = ("studentId", "gender")
    search_fields = ("studentId",)
    ordering = ("studentId",)
    
admin.site.register(Student, StudentAdmin)