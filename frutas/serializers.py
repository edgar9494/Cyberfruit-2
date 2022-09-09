# import sereliazers from the REST framework
from rest_framework import serializers
  
# import the todo data model
from .models import Usuario
  
# create a sereliazer class

class UsuarioSerializer(serializers.ModelSerializer):
  
    # create a meta class
    class Meta:
        model = Usuario
        fields = ('Rut','Password','rol')        