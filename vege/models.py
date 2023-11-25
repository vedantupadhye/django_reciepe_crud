from django.db import models

# Create your models here.
class Reciepe (models.Model):
    reciepe_name = models.CharField( max_length=100)
    reciepe_description = models.TextField()
    reciepe_image = models.ImageField(upload_to="reciepe", null = True , blank = True )


class Car(models.Model):
    car_name = models.CharField (max_length=50)
    speed = models.IntegerField(default = 50)

    def __str__(self) ->str:
        return self.car_name
         