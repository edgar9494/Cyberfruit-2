from django.db import models
  
class Usuario(models.Model):
    Rut=models.CharField(max_length=150)
    Password=models.CharField(max_length=500)
    rol=models.IntegerField(default=False)
  
    # string representation of the class
    def __str__(self):
  
        #it will return the title
        return self.Rut 