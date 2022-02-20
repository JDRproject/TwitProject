from django.db import models

# Create your models here.
class Twits(models.Model):
    user_id = models.CharField(max_length=50)
    text = models.TextField()
    
    def __str__(self):
        return [self.id ,self.user_id, self.text]