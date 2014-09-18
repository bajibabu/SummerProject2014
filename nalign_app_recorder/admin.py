from django.contrib import admin

# Register your models here.

from nalign_app_recorder.models import InputFile


class InputFilesAdmin(admin.ModelAdmin):
	list_display = ('id', 'uid')
	

   
    
admin.site.register(InputFile)

