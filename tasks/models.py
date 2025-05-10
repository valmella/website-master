from django.db import models
from django.contrib.auth.models import User
from rest_framework import generics

# Admin  
class Admin(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, default='admin')

    def __str__(self):
        return self.nombre

# Usuario independiente 
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

# Categoría de videojuego
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_categoria

# Videojuego
class Videojuego(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='videojuegos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.titulo

# Cliente del sistema
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Pedido
class Pedido(models.Model):
    fecha_pedido = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Pedido #{self.id} - Cliente: {self.cliente.nombre}"

# Detalle de cada juego comprado en un pedido
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.videojuego.titulo} x{self.cantidad}"

# Registro de pagos
class Pago(models.Model):
    metodo = models.CharField(max_length=50, null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.metodo} - ${self.monto}"

# Carrito asociado al usuario
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

# Detalle del carrito: qué juegos hay y cuántos
class DetalleCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.videojuego.titulo} x{self.cantidad}"

# Vista basada en clase para registrar pagos (API)
class PagoCreateAPIView(generics.CreateAPIView):
    queryset = Pago.objects.all()

    def get_serializer_class(self):
        from .serializers import PagoSerializer
        return PagoSerialize


