from django.contrib import admin
from .models import Record
# Register your models here.

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'pin_code', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    list_per_page = 20