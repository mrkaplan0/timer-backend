from django.contrib import admin
from core.models import *
# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id','date','note','priority']

    class Meta:
        model = Note
