from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from tasks import views
from django.contrib import admin  
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),   
    path('admin/', views.vista_admin, name='admin'),  
    path('admin-panel/', admin.site.urls),   
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('contacto/', views.contacto, name='contacto'),
    path('accion/', views.accion, name='accion'),
    path('aventura/', views.aventura, name='aventura'),
    path('carreras/', views.carreras, name='carreras'),
    path('deporte/', views.deporte, name='deporte'),
    path('estrategia/', views.estrategia, name='estrategia'),
    path('ingenio/', views.ingenio, name='ingenio'),
    path('rpg/', views.rpg, name='rpg'),
    path('carrito/', views.carrito, name='carrito'),
    path('guardar-carrito/', views.guardar_carrito, name='guardar_carrito'),
    path('pago/', views.pago_view, name='pago'),
    path('procesar-pago/', views.procesar_pago, name='procesar_pago'),
    path('usuarios/', views.obtener_usuarios),
    path('usuarios/<int:id>/', views.obtener_usuario),
    path('usuarios/crear/', views.crear_usuario),
    path('usuarios/actualizar/<int:id>/', views.actualizar_usuario),
    path('usuarios/eliminar/<int:id>/', views.eliminar_usuario),
    path('crear-roles/', views.crear_roles),
    path('asignar-rol/', views.asignar_rol),
    path('cliente/', views.vista_cliente, name='cliente'),   
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
