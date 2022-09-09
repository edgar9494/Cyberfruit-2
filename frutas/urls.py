from django.urls import path,include 
from frutas import views 
from django.contrib import admin
urlpatterns = [
     path('admin/', admin.site.urls),
  
    path('api/usuarios/',views.UsuarioView ,name="usuarios"),
    
    path('logear/',views.login ,name="login"),
    
]

