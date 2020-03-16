from django.db import models


class TVshow(models.Model):
    #ID
    title= models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    release_date=models.DateField()
    desc = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"<TVshow object: {self.title}({self.id})>"
    #networks
