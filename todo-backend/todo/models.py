from django.db import models
from users.models import User
# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=255)
    timestamp = models.DateField(auto_now_add=True)
    place = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    
    def __str__(self):
        return self.title 
    
    
    