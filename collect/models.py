from django.db import models

# Create your models here.
class Tweet(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.DateField()

    
    def __str__(self):
        return str([self.id ,self.user_id, self.text])