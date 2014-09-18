from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from nalign_app_recorder import views
	

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^files_upload$', views.upload_files),
    url(r'^output_files$', views.output_files),
    
    
)

urlpatterns=format_suffix_patterns(urlpatterns)

