from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer ,UploadSerializer 
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .models import Upload


# Create your views here.

class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny,]

    def post(self,request,*args,**kwargs):
        data=request.data
        data['username']=data.get('email')
        serializer=self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,})


class LoginView(generics.RetrieveAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny,]
    queryset = User.objects.all()

    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return Response({"message ": "login successfully "}, status=status.HTTP_200_OK)

class UploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = UploadSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UploadCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UploadSerializer
    permission_classes = [IsAuthenticated]
    queryset = Upload.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)