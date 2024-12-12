"""mipaginaweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pagina import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginPage,name='Loginhome'),
    path('contacto/', views.contacto,name='contacto'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('principal/', views.principal, name='principal'),
    path('ingreso/', views.ingreso, name='ingreso'),
    path('ingresar_suplemento/', views.ingresar_suplemento, name='ingresar_suplemento'),
    path('guardar_suplemento/', views.guardar_suplemento, name='guardar_suplemento'),
    path('login/', views.login, name='login'),
    path('loginPage/', views.loginPage, name='loginPage'),
    path('register/', views.registerPage, name='register'),
    path('actividad/', views.actividad, name='actividad'),
    path('actividad/agregarComida/', views.agregarComida, name='agregarComida'),
    path('actividad/delete_comida/', views.delete_comida, name='delete_comida'),
    path('delete/<int:id>', views.deleteSuplemento, name='delete'),
    path('update/<int:id>', views.guardar_suplemento, name='update'),
]
