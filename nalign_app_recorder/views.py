from django.shortcuts import render,render_to_response
from django.template import RequestContext

import json
from django.http import Http404, HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from nalign_app_recorder.forms import *
from nalign_app_recorder.models import InputFile

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from Nalign_Django.views import login_user

# REST Framework
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.parsers import YAMLParser,FileUploadParser,JSONParser
from rest_framework.decorators import api_view, authentication_classes,permission_classes

# Provider OAuth2
from provider.oauth2.models import Client

#From DRF
from webservice.serializers import FileSerializer
#from webservice.permissions import IsOwnerOrReadOnly

import datetime
# Create your views here.

#Registration using DRF
class RegistrationView(APIView):
    permission_classes = ()

    def post(self, request):
        serializer = RegistrationSerializer(data=request.DATA)
	print 'inside post'
        # Check format and unique constraint
        if not serializer.is_valid():
            return Response(serializer.errors,\
                            status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data
        u = User.objects.create(username=data['username'])
        u.set_password(data['password'])
        u.save()

        # Create OAuth2 client
        name = u.username
        client = Client(user=u, name=name, url='' + name,\
                client_id=name, client_secret='', client_type=1)
        client.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


#File Upload using DRF

class FileView(APIView):
    
    permission_classes = (IsAuthenticated,) # explicit
    parser_classes = (FileUploadParser,)
    print 'Inside FileView'
    
    def get(self, request):
    	print 'get method in FileView'
    	print request.FILES
    	queryset=InputFile.objects.all()
        files = InputFile.objects.filter(input_user=request.user.id)
        serializer = FileSerializer(files, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, filename, format=None):
        print 'post method in FileView'
        
        serializer = FileSerializer(data=request.DATA)
        print request.FILES
        if not serializer.is_valid():
            return Response(serializer.errors, status=
                status.HTTP_400_BAD_REQUEST)
        else:
            data = serializer.data
            input_user = request.user
            t = File(input_user=input_user, audio_file=request.FILES)
            t.save()
            request.DATA['id'] = t.pk # return id
            return Response(request.DATA, status=status.HTTP_201_CREATED)

    def put(self, request, file_id):
    	print 'inside PUT method'
        serializer = FileSerializer(data=request.DATA)
        if not serializer.is_valid():
            return Response(serializer.errors, status=
                status.HTTP_400_BAD_REQUEST)
        else:
            data = serializer.data
            t = InputFile(id=inputfile_id, input_user=request.user, audio_file=request.FILES,\
                     rec_date=datetime.now())
            t.save()
            return Response(status=status.HTTP_200_OK)
    model = InputFile
    serializer_class = FileSerializer

@login_required(login_url='/login')
def home(request):	
	
	if request.method == 'POST':
		form1 = AuthForm(request.POST)
		
		if form1.is_valid():
			check_box=form1.cleaned_data['check_box']
			return HttpResponseRedirect('files_upload')
	else:
		form1 = AuthForm()
	 

	return render(request, 'recorder.html', {
        'form': form1,
    })


@login_required(login_url='/login')
def upload_files(request):
	form=UploadFileForm()
	if request.method=='POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			obj=form.save(commit=False)
			obj.input_user=request.user
			obj.rec_date=datetime.datetime.now()
			obj.save()
	                return HttpResponseRedirect('output_files')
	else:
		form=UploadFileForm()
	
	return render(request, 'files_upload.html', {'form': form})
	
	
	
@login_required(login_url='/login')
def output_files(request):
	return render_to_response('output_files.html')

#@csrf_exempt	
#@api_view(['POST','GET'])
#@authentication_classes((SessionAuthentication, BasicAuthentication))
#@permission_classes((IsAuthenticated,))
#@login_required(login_url='/login')
def recorder2(request):
		
	#return render(request, 'recorder2.html', {'form': form_rec})
	return render_to_response('recorder2.html',RequestContext(request))

@csrf_exempt	
@api_view(['POST','GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def upload_audio(request):
	
	print 'in upload_audio'
	print request.method
	print request.is_ajax()
	print request.FILES
	if request.method=='POST' or request.is_ajax():
		
		serializer = FilesSerializer(data=request.DATA, files=request.FILES)
		if serializer.is_valid():
			print "Yaaaayy!!!!!"
			audio_file=request.FILES
	
			input_user=request.user
			rec_date=datetime.datetime.now()

	        	return HttpResponseRedirect('output_files')
		return Response(content)
	
		        	
	
def regd(request):	
	
	if request.method=='POST':
		form2 = UserRegdForm(request.POST)
		if form2.is_valid():
			new_user = User.objects.create_user(**form2.cleaned_data)
			#login_user(new_user)
	                return HttpResponseRedirect('thank_you')
	else:
		form2=UserRegdForm()
	
	return render(request, 'registration.html', {'form': form2})
	
def thank_you(request):	
	return render_to_response('thank_you.html')
	
def mic_level(request):	
	return render_to_response('mic_level.html')
	



	
