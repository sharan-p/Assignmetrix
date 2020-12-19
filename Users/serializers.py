from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Upload

class UserSerializer(serializers.ModelSerializer):
        model=User
        fields=('id','username','email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email','password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_date):
        user=user.objects.create_user(validateed_date['username'],validated_date['email'],validated_date['password'])   

        return user       

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('email','password')         

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Upload
        fields='__all__'  