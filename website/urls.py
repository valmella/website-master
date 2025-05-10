from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from tasks import views
from django.contrib import admin  
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Vistas principales
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('cliente/', views.vista_cliente, name='cliente'),
    path('tasks/', views.tasks, name='tasks'),
    path('contacto/', views.contacto, name='contacto'),

    # Categorías de videojuegos
    path('accion/', views.accion, name='accion'),
    path('aventura/', views.aventura, name='aventura'),
    path('deportes/', views.deporte, name='deporte'),
    path('estrategia/', views.estrategia, name='estrategia'),

    # Carrito y pagos
    path('carrito/', views.carrito, name='carrito'),
    path('guardar-carrito/', views.guardar_carrito, name='guardar_carrito'),
    path('pago/', views.pago_view, name='pago'),
    path('procesar-pago/', views.procesar_pago, name='procesar_pago'),

    # API Usuarios
    path('api/usuarios/', views.obtener_usuarios),
    path('api/usuarios/<int:id>/', views.obtener_usuario),
    path('api/usuarios/crear/', views.crear_usuario),
    path('api/usuarios/actualizar/<int:id>/', views.actualizar_usuario),
    path('api/usuarios/eliminar/<int:id>/', views.eliminar_usuario),

    # API Videojuegos
    path('api/videojuegos/', views.listar_videojuegos, name='listar_videojuegos'),
    path('api/videojuegos/<int:id>/', views.detalle_videojuego, name='detalle_videojuego'),

    # API Pagos
    path('api/pagos/registrar/', views.PagoCreateAPIView.as_view(), name='registrar-pago'),

    # Administración de usuarios
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),

    # Roles
    path('crear-roles/', views.crear_roles),
    path('asignar-rol/', views.asignar_rol),

     # Recuperación de contraseña
    path('restablecer-contrasena/', auth_views.PasswordResetView.as_view(), name='restablecer_contrasena'),
    path('restablecer-contrasena/completo/', auth_views.PasswordResetCompleteView.as_view(), name='restablecer_contrasena_completo'),

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)