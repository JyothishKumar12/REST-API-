from attr import field
from django.contrib import admin
from pymysql import TimestampFromTicks
from .models import Task
# Register your models here.
@admin.register(Task)


class TaskAdmin(admin.ModelAdmin):
    fields = ['title','completed']