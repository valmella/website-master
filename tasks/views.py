from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import VideojuegoForm, UsuarioForm
from .models import Videojuego, Usuario, Pago
import json
from django.http import JsonResponse
import requests

# Vistas principales
def home(request):
    return render(request, 'home.html')

def vista_admin(request):
    return render(request, 'admin.html')

def signin(request):
    if request.method == 'POST':
        # Lógica de inicio de sesión
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'signin.html', {'error': 'Credenciales inválidas'})
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        # Lógica de registro de usuario
        return redirect('signin')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def editar_perfil(request):
    return render(request, 'editar_perfil.html')

def vista_cliente(request):
    return render(request, 'cliente.html')

def tasks(request):
    return render(request, 'tasks.html')

def contacto(request):
    return render(request, 'contacto.html')

# Categorías de videojuegos
def accion(request):
    return render(request, 'accion.html')

def aventura(request):
    return render(request, 'aventura.html')

def carreras(request):
    return render(request, 'carreras.html')

def deporte(request):
    return render(request, 'deporte.html')

def estrategia(request):
    return render(request, 'estrategia.html')

def ingenio(request):
    return render(request, 'ingenio.html')

def rpg(request):
    return render(request, 'rpg.html')

# Carrito y pagos
def carrito(request):
    return render(request, 'carrito.html')

def guardar_carrito(request):
    return JsonResponse({"status": "Carrito guardado"})

def pago_view(request):
    return render(request, 'pago.html')

def procesar_pago(request):
    return JsonResponse({"status": "Pago procesado"})

# API de usuarios
def obtener_usuarios(request):
    # Lógica para obtener todos los usuarios
    return JsonResponse({"usuarios": []})

def obtener_usuario(request, id):
    # Lógica para obtener un usuario por ID
    return JsonResponse({"usuario": {}})

def crear_usuario(request):
    # Lógica para crear un usuario
    return JsonResponse({"status": "Usuario creado"})

def actualizar_usuario(request, id):
    # Lógica para actualizar un usuario
    return JsonResponse({"status": "Usuario actualizado"})

def eliminar_usuario(request, id):
    # Lógica para eliminar un usuario
    return JsonResponse({"status": "Usuario eliminado"})

# API de videojuegos
def listar_videojuegos(request):
    # Lógica para listar videojuegos
    return JsonResponse({"videojuegos": []})

def detalle_videojuego(request, id):
    # Lógica para obtener detalles de un videojuego por ID
    return JsonResponse({"videojuego": {}})

# Administración de usuarios
def lista_usuarios(request):
    return render(request, 'lista_usuarios.html')

def editar_usuario(request, id):
    return render(request, 'editar_usuario.html')

def eliminar_usuario(request, id):
    return redirect('lista_usuarios')

# Gestión de roles
def crear_roles(request):
    return render(request, 'crear_roles.html')

def asignar_rol(request):
    return render(request, 'asignar_rol.html')

# Recuperación de contraseña (estas vistas están integradas con Django)
from django.contrib.auth import views as auth_views

password_reset_view = auth_views.PasswordResetView.as_view()
password_reset_done_view = auth_views.PasswordResetDoneView.as_view()
password_reset_confirm_view = auth_views.PasswordResetConfirmView.as_view()
password_reset_complete_view = auth_views.PasswordResetCompleteView.as_view()


class PagoCreateAPIView(generics.CreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer