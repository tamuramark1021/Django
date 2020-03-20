from django.db import models
import re
import bcrypt
import datetime

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        # now=datetime.datetime.now()
        if len(postData['first_name'])<2:
            errors['first_name']="This field must have at least 2 character"
        if len(postData['last_name'])<2:
            errors['last_name']="This field must have at least 2 character"
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email_register']):
            errors['email']= "invalid email address!"
        elif len(User.objects.filter(email=postData['email_register'])) > 0:
            errors['email'] = "This email already has an account"
        if len(postData['password_register'])<8:
            errors['password_register']="This field must have at least 8 characters"
        elif postData['password_register'] != postData['confirm_password']:
            errors['password_register'] = "Passwords do not match!"
        # if postData['dob']>=now:
        #     errors['dob']= "Invalid date, please try again"
        
    def login_validator(self, postData):
        errors={}
        # valid_login={
        #     'errors':{},
        # }
        # user=self.filter(email=postData['email_login'])
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        user = User.objects.filter(email=postData['email_login'])
        if not EMAIL_REGEX.match(postData['email_login']):
            errors['email_login']= "Email is invalid"
        elif not user:
            errors['email_login'] = "This email does not exist homey!"
        else: 
            if len(postData['password_login']) < 8:
                errors['email_login'] = "Password needs to be at least 8 characters"
            elif bcrypt.checkpw(postData['password_login'].encode(), user[0].password.encode()):
                print("Passwords Match!")
            else:
                errors['password_login'] = "This is not a valid password"
        return errors

        # if len(postData)['password_login'] <8:
        #     errors['password_login']= "This field must have at least 8 characters"
        # elif not user:
        #     errors['email_login']= "Email not on file, please register!"
        # else:
        #     errors['user']=user[0]
        #     elif not bcrypt.checkpw(postData['password_login'].encode(), user[0].password.encode()):
        #         errors['password_login']="Not a valid password, please try again"
        # return errors

class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

    # def basic_validator(self, postData):
    #     errors={}
    #     if len(postData['first_name'])<1:
    #         errors['first_name']="This field must have at least 1 character"
    #     if len(postData['last_name'])<1:
    #         errors['last_name']="This field must have at least 1 character"
    #     EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    #     if not EMAIL_REGEX.match(postData['email']):
    #         errors['email']= "invalid email address!"
    #     if len(postData['password'])<7:
    #         errors['password']="This field must have at least 8 characters"

    # def login_validator(self, postData):
    #     # valid_login={
    #     #     'errors':{},
    #     # }
    #     errors={}
    #     user=self.filter(email=postData['email'])
    #     EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    #     if not EMAIL_REGEX.match(postData['email']):
    #         valid_login['errors']['email']= "Email is invalid"
    #     elif not user:
    #         valid_login['errors']['email']= "Email not on file, please register!"
    #     else:
    #         valid_login['user']=user[0]
    #         if len(postData)['password']<8:
    #             valid_login['errors']['password']= "This field must have at least 8 characters"
    #         elif not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
    #             valid_login['errors']['password']="Not a valid password, please try again"
    #     return errors #valid_login
    
