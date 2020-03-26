from django.db import models
from login_app.models import User
# Create your models here.
class Validator(models.Manager):
    def book_validator(self, postData):
        errors={}
        if len(postData['title'])<1:
            errors['title']='This field must have at least 2 characters'
        if len(postData['author'])<1:
            errors['author']='This field must have at least 2 characters'
        if len(postData['content'])<1:
            errors['content']='This field must have at least 2 characters'
        if len(postData['rating'])<0:
            errors['rating']='Must select a rating'
        return errors

class Book(models.Model):#dont forget to capitalize class name
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='book')#one to many field name
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    rating=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=Validator()

class Review(models.Model):
    content=models.CharField(max_length=255)
    book=models.ForeignKey(Book, on_delete=models.CASCADE, related_name='review')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    