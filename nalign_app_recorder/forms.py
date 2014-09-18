
from django.forms import ModelForm
from django import forms
from nalign_app_recorder.models import InputFile
from django.contrib.auth.models import User

class AuthForm(forms.Form):   #This is used when the audio is downloaded - recorder.html
    check_box = forms.BooleanField(required=False) #Just a dummy variable (The webpage uses form method and hence a dummy form is used)



class UploadFileForm(ModelForm): #This is for uploading audio files
	class Meta:
	    	model = InputFile
	    	fields = ('audio_file',)
	    	
	    	
class UserRegdForm(ModelForm): # For user registration
	class Meta:
	    	model = User
	    	fields = ('username', 'first_name', 'last_name', 'email', 'password')
	    	
