from django.db import models

from django.db import models

class Person(models.Model):
    first_name=models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    age = models.IntegerField()


    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
