from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    subject = models.CharField(max_length=500, blank=True, null=True)
    deaadline = models.DateTimeField(blank=True, null=True)
    # timezone=
    academiclevels = models.CharField(max_length=500, blank=True, null=True)
    file_upload = models.FileField(blank=True, null=True)
