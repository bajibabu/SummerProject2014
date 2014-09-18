from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from nalign_app_recorder import views

from django.contrib import admin
admin.autodiscover()

#From "webservices" folder....DRF
#from webservice.api import UserList, UserDetail
from webservice.api import FileList, FileDetail, UserFileList



file_urls = patterns('',
    #url(r'^/(?P<pk>\d+)/files$', PostFileList.as_view(), name='postfile-list'),
    url(r'^/(?P<pk>\d+)$', FileDetail.as_view(), name='file-detail'),
    url(r'^$', FileList.as_view(), name='file-list')
)



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Nalign_Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   #To vies the admin page
    url(r'^admin/', include(admin.site.urls)),
   
    #Mic Level
    url(r'^mic_level$', 'nalign_app_recorder.views.mic_level'),
    
    #Recording
    url(r'^wavs/',include('nalign_app_recorder.urls')),
    url(r'^wavs2/$', 'nalign_app_recorder.views.recorder2'),
    #Note: generalize the path of recorderWorker.js (it is hard-coded now)........
    
    #Login
    url(r'^login/$', 'Nalign_Django.views.login_user', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),  
    
    #Registration
    url(r'^regd/$', 'nalign_app_recorder.views.regd'),
    
    #Thank you page
    url(r'thank_you/$', 'nalign_app_recorder.views.thank_you', name='thank_you'),
    
    #File upload (using AJAX JQuery)
    url(r'upload_audio/$', 'nalign_app_recorder.views.upload_audio'),
    
    #File Upload....using DRF
    url(r'^files/$', views.FileView.as_view()),
    url(r'^files/(?P<file_id>[0-9]*)$', views.FileView.as_view()),
    
    #Registration using DRF
    url(r'^reg/$', views.RegistrationView.as_view()),
    
    # API authentication
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^api-auth/', include('rest_framework.urls',\
        namespace='rest_framework')),

    #From webservices/api.py
    #url(r'^users', include(user_urls)),
    url(r'^posts', include(file_urls)),

   
)+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()


