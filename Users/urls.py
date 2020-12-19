from .views import RegisterApi,LoginView,UploadView,UploadCreateAPIView
from django.urls import path

urlpatterns=[
    path('register/',RegisterApi.as_view(),name='register'),
    path('login/',view=LoginView.as_view(),name='login'),
    path('upload/', UploadView.as_view(), name='file-upload'),
  	path('data/', UploadCreateAPIView.as_view(), name='data'),
]