 from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import VideojuegoForm, UsuarioForm
from .models import Videojuego, Usuario, Pago
import json
from django.http import JsonResponse

# Funciones para vistas basadas en formularios, creación de usuarios, autenticación, etc.
def home(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'index.html', {'videojuegos': videojuegos})

@login_required
@csrf_exempt
def guardar_carrito(request):
    if request.method == 'POST':
        cart_data = request.POST.get('cart_data', '[]')
        carrito = json.loads(cart_data)

        for item in carrito:
            Pago.objects.create(
                usuario=request.user,
                nombre_producto=item['name'],
                cantidad=item['quantity'],
                precio_unitario=item['price'],
                total=item['price'] * item['quantity']
            )

        return JsonResponse({'status': 'ok', 'message': 'Carrito guardado con éxito'})
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'})

@login_required
def pago_view(request):
    total = request.session.get('cart_total', 0)
    return render(request, 'pago.html', {'total': total})

# Para roles de usuarios
def crear_roles(request):
    Group.objects.get_or_create(name='Administrador')
    Group.objects.get_or_create(name='Cliente')
    return render(request, 'roles_creados.html')

def asignar_rol(request):
    usuario = User.objects.get(username='valentina')
    grupo = Group.objects.get(name='Administrador')
    usuario.groups.add(grupo)
    return render(request, 'rol_asignado.html')

# Vistas para editar perfil de usuario
def editar_perfil(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = UserChangeForm(instance=request.user)
    
    return render(request, 'editar_perfil.html', {'form': form})


