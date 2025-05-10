from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from tasks import views
from django.contrib import admin  
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Vistas principales
    path('', views.home, name='home'),
    path('admin/', views.vista_admin, name='admin'),
    path('admin-panel/', admin.site.urls),
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
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
