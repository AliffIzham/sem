from django.db import models


# Create your models here.

class Item(models.Model):
    idnum = models.TextField(max_length=15, null=True)
    dateIn = models.DateField(max_length=100, null=True)
    dateOut = models.DateField(max_length=100, null=True)
    Stats = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.idnum}{self.dateIn}{self.dateOut}{self.Stats}'



