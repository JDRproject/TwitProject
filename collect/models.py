from django.db import models

# Create your models here.
class Tweet(models.Model):

    name = models.CharField(max_length=50)
    text = models.TextField(null=True)
    time = models.DateTimeField(null=True)
    grade_rawmeat = models.IntegerField(default=-1, null=True)
    grade_maratang = models.IntegerField(default=-1,null=True)
    grade_crab = models.IntegerField(default=-1,null=True)
    grade_seonji = models.IntegerField(default=-1,null=True)
    grade_mincho = models.IntegerField(default=-1,null=True)
    grade_sparkling = models.IntegerField(default=-1,null=True)
    grade_coffee = models.IntegerField(default=-1,null=True)
    grade_oysters = models.IntegerField(default=-1,null=True)
    grade_chicken_foot = models.IntegerField(default=-1,null=True)
    grade_makchang = models.IntegerField(default=-1,null=True)
    grade_gobchang = models.IntegerField(default=-1,null=True)
    grade_chicken_coop= models.IntegerField(default=-1,null=True)
    grade_altang = models.IntegerField(default=-1,null=True)
    grade_nakgi = models.IntegerField(default=-1,null=True)
    grade_odeng = models.IntegerField(default=-1,null=True)
    grade_lamb = models.IntegerField(default=-1,null=True)
    grade_ddukboki = models.IntegerField(default=-1,null=True)
    test = models.IntegerField(default=-1,null=True)

    
    def __str__(self):
        return str([self.name , self.text])