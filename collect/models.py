from django.db import models

# Create your models here.
class Tweet(models.Model):

    name = models.CharField(max_length=50)
    text = models.TextField()
    time = models.DateTimeField()
    grade_rawmeat = models.IntegerField(null=True)
    grade_maratang = models.IntegerField(null=True)
    grade_crab = models.IntegerField(null=True)
    grade_seonji = models.IntegerField(null=True)
    grade_mincho = models.IntegerField(null=True)
    grade_sparkling = models.IntegerField(null=True)
    grade_coffee = models.IntegerField(null=True)
    grade_oysters = models.IntegerField(null=True)
    grade_chicken_foot = models.IntegerField(null=True)
    grade_makchang = models.IntegerField(null=True)
    grade_gobchang = models.IntegerField(null=True)
    grade_chicken_coop= models.IntegerField(null=True)
    grade_altang = models.IntegerField(null=True)
    grade_nakgi = models.IntegerField(null=True)
    grade_odeng = models.IntegerField(null=True)
    grade_lamb = models.IntegerField(null=True)
    grade_ddukboki = models.IntegerField(null=True)

    
    def __str__(self):
        return str([self.name , self.text])