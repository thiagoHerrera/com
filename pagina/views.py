from django.shortcuts import redirect, render, HttpResponse
from pagina.models import Agenda
from pagina.models import Suplemento
from django.shortcuts import render
from .forms import SuplementoForm
from .models import Food
from .forms import FoodForm
# Users
from django.contrib.auth.forms import UserCreationForm
from pagina.forms import RegisterForm 
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request, "./index.html")

def contacto(request):
    return render(request, "./contacto.html")

def plantilla(request):
    return render(request, "./plantilla.html")

def iniciar_sesion(request):    
    return render(request, "./iniciar_sesion.html")

def principal(request):
    return render(request, "./principal.html")

def ingreso(request):
    if request.method == 'POST':
        form = SuplementoForm(request.POST, request.FILES)  
        if form.is_valid():
            form.save()  
            return redirect('ingreso')  
    else:
        form = SuplementoForm()

    suplementos = Suplemento.objects.all()
    return render(request, 'ingreso.html', {'form': form, 'suplementos': suplementos})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")
        user = authenticate(request, username=username,password = password)
        
        if user is not None:
            login(request, user)
            return redirect('principal')  
        else:
            return render(request, './login.html', {'error': 'Usuario o contraseña incorrectos.'})
    
    return render(request, './login.html')

def registerPage(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('principal')  
    else:
        register_form = RegisterForm()

    return render(request, './register.html', {'register_form': register_form})

def suplementos_page(request):
    suplementos = Suplemento.objects.all()  
    return render(request, 'ingreso.html', {'suplementos': suplementos})

def ingresar_suplemento(request):
    return render(request, 'ingresar_suplemento.html')

def guardar_suplemento(request, id=None):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen', None)  

        if id:
            try:
                
                suple = Suplemento.objects.get(pk=id)
                
                suple.nombre = nombre
                suple.descripcion = descripcion
                if imagen:  
                    suple.imagen = imagen
                
                suple.save()  
            except Suplemento.DoesNotExist:
                return redirect('error_page') 
        else:
            suplemento = Suplemento(nombre=nombre, descripcion=descripcion, imagen=imagen)
            suplemento.save()

        return redirect('ingreso')

    else:
        if id:
            try:
                suple = Suplemento.objects.get(pk=id)
                return render(request, 'modificar.html', {'suplemento': suple})
            except Suplemento.DoesNotExist:
                return redirect('error_page')
        return render(request, 'ingresar_suplemento.html')
    
    
    

def deleteSuplemento(request,id):
	suple = Suplemento.objects.get(pk = id)
	suple.delete()
	return redirect('ingreso')

def actividad(request):
    foods = Food.objects.all()
    return render(request, 'actividad.html', {'foods': foods})

def agregarComida(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('actividad')  
    else:
        form = FoodForm()
    return render(request, 'actividad.html', {'form': form})

def delete_comida(request):
    if request.method == 'POST':
        food_id = request.POST.get('food_id')
        food = Food.objects.get(id=food_id)
        food.delete()
        return redirect('actividad')


#el filter deja pasar por parametros los campos que tenemos. filter(parametro=,parametro=)
