from rest_framework import generics, permissions


from webservice.serializers import  RegistrationSerializer, FileSerializer
from nalign_app_recorder.models import InputFile
from django.contrib.auth.models import User
from webservice.permissions import SafeMethodsOnlyPermission, PostAuthorCanEditPermission



class FileList(generics.ListCreateAPIView):
    model = InputFile
    serializer_class = FileSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    model = InputFile
    serializer_class = FileSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UserFileList(generics.ListAPIView):
    model = InputFile
    serializer_class = FileSerializer

    def get_queryset(self):
        queryset = super(UserFileList, self).get_queryset()
        return queryset.filter(input_user__username=self.kwargs.get('username'))


class PostMixin(object):
    model = InputFile
    serializer_class = FileSerializer
    permission_classes = [
        PostAuthorCanEditPermission
    ]

    def pre_save(self, obj):
        """Force author to the current user on save"""
        obj.input_user = self.request.user
        return super(PostMixin, self).pre_save(obj)


class FileList(PostMixin, generics.ListCreateAPIView):
    pass


class FileDetail(PostMixin, generics.RetrieveUpdateDestroyAPIView):
    pass


