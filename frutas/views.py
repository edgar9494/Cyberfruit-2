from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
# import the TodoSerializer from the serializer file
from .serializers import UsuarioSerializer
  
# import the Todo model from the models file
from .models import Usuario
  
# create a class for the Todo model viewsets
class UsuarioView(viewsets.ModelViewSet):
  
    # create a sereializer class and 
    # assign it to the TodoSerializer class
    serializer_class = UsuarioSerializer
  
    # define a variable and populate it 
    # with the Todo list objects
    queryset = Usuario.objects.all()

@ api_view(['POST'])
def login(request):
    if request.method == 'POST':
        rut= request.data.get('usu_rut')
        rut = request.data["usu_rut"]
        rut = rut.replace("-","")
        rut = rut.replace(".","")
        rut = rut.lower()
        
        contraseña= request.data.get('usu_contraseña')
        usu = Usuario.objects.filter(Rut= rut).first()
        if usu!= None:
            if usu.Password ==contraseña:
                return Response({'cargo' :usu.rol,'estado':1,'rut':usu.Rut})
            else:
                return Response({'cargo' :usu.rol,'estado':2})
        else:
            return Response({'estado':3})       