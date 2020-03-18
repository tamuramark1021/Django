from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import datetime



    #networks

class TVshow_manager(models.Model):
    def basic_validator(self, postData):
        now=datetime.datetime.now()
        today8am=now.replace(hour=8,minute=0, second=0, microsecond=0)
        # now== today8am
        #     False 
        # now>today8am
        #     False 
        errors={}
        release_date_input=input('dd/mm/yyyy')
        day,month,year=release_date_input.split('/')
        isValidDate=True
        try:
            datetime.datetime(int(year),int(month),int(day))
        except ValueError:
            isValidDate=False
        if(isValidDate):
            print('input date is valid')
        else:
            print("input date is not valid")    
        # EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # if not EMAIL_REGEX.match(postDATA['email']):
            # errors['email']= "invalid email address!"        
        if len(postData['title'])<1:
            errors['title']="Title name must have at least 2 characters"
        if len(postData['network'])<2:
            errors['network']= "Network name must have at least 3 characters"
        if now<today8am:
            True
        else:
            False
            # errors['release_date']="Release date musst be a past date")
        if len(postData['desc'])<9:
            errors['desc']="Description should have at least 10 characters"
        return errors
        
class TVshow(models.Model):
    #ID
    def basic_validator(self, postData):
        now=datetime.datetime.now()
        today8am=now.replace(hour=8,minute=0, second=0, microsecond=0)
        # now== today8am
        #     False 
        # now>today8am
        #     False 
        errors={}
        release_date_input=input('dd/mm/yyyy')
        day,month,year=release_date_input.split('/')
        isValidDate=True
        try:
            datetime.datetime(int(year),int(month),int(day))
        except ValueError:
            isValidDate=False
        if(isValidDate):
            print('input date is valid')
        else:
            print("input date is not valid")    
        # EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # if not EMAIL_REGEX.match(postDATA['email']):
            # errors['email']= "invalid email address!"        
        if len(postData['title'])<1:
            errors['title']="Title name must have at least 2 characters"
        if len(postData['network'])<2:
            errors['network']= "Network name must have at least 3 characters"
        if now<today8am:
            True
        else:
            False
            # errors['release_date']="Release date musst be a past date")
        if len(postData['desc'])<9:
            errors['desc']="Description should have at least 10 characters"
        return errors   
    title= models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    release_date=models.DateField()
    desc = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=TVshow_manager()
    def __repr__(self):
        return f"<TVshow object: {self.title}({self.id})>"