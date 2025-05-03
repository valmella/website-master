from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.db import IntegrityError
from .models import Videojuego, Pago
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import UsuarioForm   
from .models import Usuario      
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test



def home(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'index.html', {'videojuegos': videojuegos})

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'signup.html', {
                'error': 'Las contraseñas no coinciden.'
            })

        try:
            user = User.objects.create_user(
                username=username, password=password1)
            user.save()
            login(request, user)
            return redirect('tasks')
        except:
            return render(request, 'signup.html', {
                'error': 'El nombre de usuario ya existe.'
            })

def tasks(request):
    return render(request, 'tasks.html')

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # autenticación
            user = form.get_user()
            login(request, user)
            return redirect('tasks')  # redirige a taras tras iniciar sesión
        else:
            return render(request, 'signin.html', {
                'form': form,
                'error': 'Las credenciales son incorrectas.'
            })
    else:
        form = AuthenticationForm()
    
    return render(request, 'signin.html', {'form': form})

def logout_view(request):
    logout(request)  
    return redirect('signin')  # redirige al inicio de sesión

def contacto(request):
    return render(request, 'contacto.html')

def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'videojuegos/lista_videojuegos.html', {'videojuegos': videojuegos})

def crear_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm()
    return render(request, 'videojuegos/crear_videojuego.html', {'form': form})
    
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
    
def carrito(request):
    return render(request, 'carrito.html')

def add_to_cart(request, product_id):
    product = get_object_or_404(Videojuego, id=product_id)
    cart = request.session.get('cart', {})

    if product.id in cart:
        cart[product.id]['quantity'] += 1
    else:
        cart[product.id] = {
    'name': product.titulo,  
    'price': product.precio,
    'quantity': 1
}

    request.session['cart'] = cart
    return redirect('carrito')

def view_cart(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    request.session['cart_total'] = total   
    return render(request, 'carrito.html', {'cart': cart, 'total': total})

@login_required
@csrf_exempt
def guardar_carrito(request):
    if request.method == 'POST':
        cart_data = request.POST.get('cart_data', '[]')
        carrito = json.loads(cart_data)

        # guardar productos en la base de datos  
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

#  mostrar el pago
@login_required
def pago_view(request):
    total = request.session.get('cart_total', 0)
    return render(request, 'pago.html', {'total': total})

def procesar_pago(request):
    # procesar el pago
    return render(request, 'nombre_template.html')

# Crear un nuevo usuario (POST)
@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = UsuarioForm()

    return render(request, 'crear_usuario.html', {'form': form})

def obtener_usuarios(request):
    usuarios = Usuario.objects.all().values('id', 'nombre', 'email', 'edad', 'direccion')
    return JsonResponse(list(usuarios), safe=False)

# obtener un usuario específico por ID
def obtener_usuario(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
        return JsonResponse({'id': usuario.id, 'nombre': usuario.nombre, 'email': usuario.email, 'edad': usuario.edad, 'direccion': usuario.direccion})
    except Usuario.DoesNotExist:
        return JsonResponse({'mensaje': 'Usuario no encontrado'}, status=404)

# actualizar un usuario 
@csrf_exempt
def actualizar_usuario(request, id):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            usuario = Usuario.objects.get(id=id)
            usuario.nombre = data['nombre']
            usuario.email = data['email']
            usuario.edad = data['edad']
            usuario.direccion = data['direccion']
            usuario.save()
            return JsonResponse({'mensaje': 'Usuario actualizado correctamente'})
        except Usuario.DoesNotExist:
            return JsonResponse({'mensaje': 'Usuario no encontrado'}, status=404)

# eliminar un usuario 
@csrf_exempt
def eliminar_usuario(request, id):
    if request.method == "DELETE":
        try:
            usuario = Usuario.objects.get(id=id)
            usuario.delete()
            return JsonResponse({'mensaje': 'Usuario eliminado correctamente'})
        except Usuario.DoesNotExist:
            return JsonResponse({'mensaje': 'Usuario no encontrado'}, status=404)

def crear_roles(request):
    Group.objects.get_or_create(name='Administrador')
    Group.objects.get_or_create(name='Cliente')
    return render(request, 'roles_creados.html')

def asignar_rol(request):
    usuario = User.objects.get(username='valentina')
    grupo = Group.objects.get(name='Administrador')
    usuario.groups.add(grupo)
    return render(request, 'rol_asignado.html')

def es_admin(user):
    return user.groups.filter(name='Administrador').exists()

def es_cliente(user):
    return user.groups.filter(name='Cliente').exists()

@login_required
@user_passes_test(es_admin)
def vista_admin(request):
    return render(request, 'admin.html')

@login_required
@user_passes_test(es_cliente)
def vista_cliente(request):
    return render(request, 'cliente.html')

def editar_perfil(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = UserChangeForm(instance=request.user)
    
    return render(request, 'editar_perfil.html', {'form': form})
