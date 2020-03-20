from django.db import models

# Create your models here.
class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    posts=models.ManyToManyField(Post, related_name='users')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Post(models.Model):
    message= models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    #users field created during makemigrations of user object


class Comment(models.Model):
    post =models.ForeignKey(Post, related_name='posts', on_delete=models.CASCADE)
    user =models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    message=models.TextField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)