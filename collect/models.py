from django.db import models

# Create your models here.
class Tweet(models.Model):

    name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.DateTimeField()
    grade_rawmeat = models.IntegerField
    grade_maratang = models.IntegerField
    grade_crab = models.IntegerField
    grade_seonji = models.IntegerField
    grade_mincho = models.IntegerField
    grade_sparkling = models.IntegerField
    grade_coffee = models.IntegerField
    grade_oysters = models.IntegerField
    grade_chicken_foot = models.IntegerField
    grade_makchang = models.IntegerField
    grade_gobchang = models.IntegerField
    grade_chicken_coop= models.IntegerField
    grade_altang = models.IntegerField
    grade_nakgi = models.IntegerField
    grade_odeng = models.IntegerField
    grade_lamb = models.IntegerField
    grade_ddukboki = models.IntegerField

    
    def __str__(self):
        return str([self.name , self.text])