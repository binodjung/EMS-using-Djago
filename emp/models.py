from django.db import models

class Employee(models.Model):
    first_name= models.CharField(max_length=50)
    salary= models.DecimalField(max_digits=7, decimal_places=2)
    age= models.IntegerField()

    def __str__(self):
        return self.first_name