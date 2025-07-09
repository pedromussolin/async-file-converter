from django.contrib import admin
from .models import FileType, Conversion

@admin.register(FileType)
class FileTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'extension', 'is_active')
    search_fields = ('name', 'extension')
    list_filter = ('is_active',)

@admin.register(Conversion)
class ConversionAdmin(admin.ModelAdmin):
    list_display = ('input_file', 'output_file', 'input_type', 'output_type', 'status', 'created_at')
    search_fields = ('input_file', 'output_file')
    list_filter = ('status', 'input_type', 'output_type')
