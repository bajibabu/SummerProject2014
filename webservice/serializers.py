from rest_framework import serializers
from django.contrib.auth.models import User
from nalign_app_recorder.models import InputFile


#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = User

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class FileSerializer(serializers.ModelSerializer):
	print 'Inside FileSerializer'
	def get_validation_exclusions(self):
        # Need to exclude `input_user` since we'll add that later based on the request
        	exclusions = super(FileSerializer, self).get_validation_exclusions()
        	return exclusions + ['input_user']

	class Meta:
		model=InputFile
		#fields=('id','audio_file')
