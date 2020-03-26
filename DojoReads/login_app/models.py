from django.db import models
import bcrypt
from django.contrib import messages
import re
# Create your models here.
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Validator(models.Manager):
    def register_validator(self, postData):
        errors={}
        if len(postData['first_name'])<1:
            errors['first_name']='This field must have at least 2 characters'
        if len (postData['last_name'])<1:
            errors['last_name']='This field must have at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']='invalid email address, please try again'
        elif len(User.objects.filter(email=postData['email']))>0:
            errors['email']='This email already has an account'
        if len(postData['password'])<7:
            errors['password']='This field must have at least 8 characters'
        elif postData['password']!=postData['password']:
            errors['password']='passwords do not match!'
        return errors

    def login_validator(self, postData):
        errors={}
        user=User.objects.filter(email=postData['email'])
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']='Email is invalid'
        elif not user:
            errors['email']='This email does not exist!'
        else:
            if not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                errors['password']='This is not a valid password'
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=Validator()