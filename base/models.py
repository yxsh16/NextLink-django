from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null = True)
    email = models.EmailField(unique = True ,null = True)
    bio = models.TextField(null = True)    

    #avatar
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null = True) # It implies that each room is associated with one user as its host, and a user can be the host of multiple rooms.
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null = True) #  It implies that each room is associated with one topic, and a topic can be associated with multiple rooms.
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    participants = models.ManyToManyField(User, related_name = 'participants', blank= True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)
    # ForeignKeys establish many-to-one relationship
    
    class Meta:
        ordering = ['-updated', '-created']
    
    
    def __str__(self):
        return self.name
    
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) 
    body = models.TextField()    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ['-updated', '-created']
    
    def __str__(self):
        return self.body[0:50]