from django.db import models
from django.contrib.auth.models import User  
  
  
class UserProfile(models.Model):  
  
    age = models.IntegerField()  
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')


class Car(models.Model):  
    MECHANIC = 1
    AUTOMATIC = 2
    ROBOT = 3
    TRANS_TYPE = [
        (MECHANIC, 'Механика'),
        (AUTOMATIC, 'Автомат'),
        (ROBOT, 'Робот')
    ]
    transmission = models.SmallIntegerField(default=MECHANIC, choices=TRANS_TYPE)
    producer = models.CharField(max_length=255)  
    model = models.CharField(max_length=255)  
    year = models.IntegerField()
    color = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='cars_photo', blank=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({}, {})".format(self.producer, self.model,
                                    self.year)
# Create your models here.
