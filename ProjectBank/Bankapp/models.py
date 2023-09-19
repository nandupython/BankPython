from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name=models.CharField(max_length=250)
    desc=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
