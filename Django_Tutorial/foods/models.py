from django.db import models


# Create your models here.
<<<<<<< Updated upstream

class Menu(models.Model):
    name = models.CharField(max_length=80)
    name_eng = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
=======
class Menu(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
>>>>>>> Stashed changes
    price = models.IntegerField()
    img_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name
