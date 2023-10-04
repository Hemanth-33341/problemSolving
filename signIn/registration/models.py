from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class form(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    mail_ID = models.CharField(max_length = 25)
    
class form2(models.Model):
    user_name=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    
    
    
