from django.db import models

from accounts.models import User
from django.urls import reverse
from django.utils.timezone import now

class Post(models.Model):
    title=models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=130)
    content=models.TextField()
    image =  models.ImageField(upload_to="posts", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.author) +  " Blog Title: " + self.title
    
    def get_absolute_url(self):
        return reverse('blogs')
