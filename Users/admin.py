from django.contrib import admin
from .models import Upload

# Register your models here.
class UploadAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'file_upload',
    )
admin.site.register(Upload,UploadAdmin)    