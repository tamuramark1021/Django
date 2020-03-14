from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<Book object: {self.title}({self.id})>"
    
class Author(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    books= models.ManyToManyField(Book, related_name="authors")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    notes=models.TextField()
    def __repr__(self):
        return f"<Author object: {self.first_name}{self.last_name}({self.id})>"
    
# class Book_author(models.Model):
#     book= models.ForeignKey(Book, related_name= "authors", on_delete=models.CASCADE)
#     author=models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)