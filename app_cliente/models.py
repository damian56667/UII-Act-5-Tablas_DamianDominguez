from django.db import models

# Create your models here.

class Cliente(models.Model):  # It's a common convention to use capitalized class names
    nombre = models.CharField(max_length=300)  # Fixed typo 'mex_length' to 'max_length'
    apellido = models.CharField(max_length=300)  # Changed from IntegerField to CharField
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"  # Updated to return both nombre and apellido