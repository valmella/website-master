from rest_framework import serializers
from .models import Videojuego
from .models import DetallePedido
from .models import Pedido
from .serializers import DetallePedidoSerializer

class PedidoSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    admin_nombre = serializers.CharField(source='admin.nombre', read_only=True)
    detalles = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = ['id', 'fecha_pedido', 'total', 'cliente_nombre', 'admin_nombre', 'detalles']

    def get_detalles(self, obj):
        detalles = DetallePedido.objects.filter(pedido=obj)
        return DetallePedidoSerializer(detalles, many=True).data

class VideojuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videojuego
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ['id', 'metodo', 'monto']

from .models import DetallePedido
from rest_framework import serializers

class PedidoSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    admin_nombre = serializers.CharField(source='admin.nombre', read_only=True)
    detalles = serializers.SerializerMethodField()

    class Meta:
        model = Pedido
        fields = ['id', 'fecha_pedido', 'total', 'cliente_nombre', 'admin_nombre', 'detalles']

    def get_detalles(self, obj):
        detalles = DetallePedido.objects.filter(pedido=obj)
        return DetallePedidoSerializer(detalles, many=True).data

class DetallePedidoSerializer(serializers.ModelSerializer):
    videojuego_titulo = serializers.CharField(source='videojuego.titulo', read_only=True)

    class Meta:
        model = DetallePedido
        fields = ['videojuego_titulo', 'cantidad', 'precio_unitario']