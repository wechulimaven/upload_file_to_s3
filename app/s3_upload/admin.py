from django.contrib import admin

from .models import Files


class FilesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Files, FilesAdmin)