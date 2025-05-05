from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import generics
from .models import Pago
from .serializers import PagoSerializer 

class Admin(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, default='admin')

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_categoria

class Videojuego(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='videojuegos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    direccion = models.TextField()

class Pedido(models.Model):
    fecha_pedido = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True)

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

class Pago(models.Model):
    metodo = models.CharField(max_length=50, null=True, blank=True)  # Permitir valores nulos
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):

        return f"{self.metodo} - {self.monto}"

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class DetalleCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

class PagoCreateAPIView(generics.CreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
