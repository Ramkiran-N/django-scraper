from django.db import models

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    link = models.CharField(max_length=2000,null=True,blank=True)

    # def __str__(self):
    #     return self.name