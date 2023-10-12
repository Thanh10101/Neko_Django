from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=20,blank=False,null=False)
    desc = models.CharField(max_length=100,blank=False,null=False)
    date = models.DateField()
    provider = models.CharField(max_length=50,blank=False,null=False)
    category = models.CharField(max_length=50,blank=False,null=False)

    def __str__(self):
        return self.name