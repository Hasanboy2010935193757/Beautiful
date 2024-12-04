from django.db import models

# Create your models here.

class Maxsulot(models.Model):
    nomi = models.CharField(max_length=20)
    bio = models.TextField()
    rasm = models.ImageField(upload_to='maxsulot/')
    narxi = models.IntegerField()


    def __str__(self):
        return self.nomi

class Rasm(models.Model):
    rasm = models.ImageField(upload_to='Rasm')
    nomi = models.CharField(max_length=60)
    bio = models.TextField()
    narxi = models.IntegerField()

    def __str__(self):
        return self.nomi
class Haridor(models.Model):
    rasm = models.ImageField(upload_to='haridor')
    nomi = models.CharField(max_length=60)
    bio = models.TextField()

    def __str__(self):
        return self.nomi



