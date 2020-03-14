from django.db import models

# # Create your models here.
# class Recipe(models.Model):
#     name=models.CharField(max_length=255)
    
# class image(models.Model):
#     url=models.URLField
#     caption=models.CharField(max_length=150)
#     alt=models.CharField(max_length=255, blank=True)

# class Recipe_Ingredient(models.Model):
#     recipe=models.ManyToManyField(recipe, through="ingredient")
#     quantity=models.IntegerField

# class Ingredient(models.Model):
#     recipet_ingredient=models.ForeignKey(
#         Recipe_Ingredient, on_delete=models.CASCADE)
#     recipe=models.ForeignKey(recipe, on_delete=models.CASCADE)
#     name=models.CharField(max_length=100)
#     fat=models.IntegerField()
#     carb=models.IntegerField()
#     protein=models.IntegerField()

class Movie(models.Model):
    title=models.CharField(max_length=45)
    description=models.TextField()
    release_date=models.DateTimeField()
    duration= models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email_addr=models.CharField(max_length=255)
    age=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)