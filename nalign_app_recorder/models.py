from django.db import models

import os
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.conf import settings
import uuid


def content_file_name(instance, filename):#Storing the file in appropriate folder (called from models.FileField in InputFile)
	path=instance.input_user.username
	return os.path.join(path, filename)
	
class InputFile(models.Model): #Model for storing audio files
	input_user = models.ForeignKey(User) 
	audio_file = models.FileField(upload_to=content_file_name)
	rec_date = models.DateTimeField('date recorded', auto_now_add=True)

	def __unicode__(self):  # Python 3: def __str__(self):
		return unicode(self.input_user.username) 	
	
        
  
		




