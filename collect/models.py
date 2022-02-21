from django.db import models

# Create your models here.
class Tweet(models.Model):

    name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.DateTimeField()

    
    def __str__(self):
        return str([self.name , self.text])