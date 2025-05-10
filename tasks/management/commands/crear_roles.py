from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from tasks.models import Tarea  
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission



class Command(BaseCommand):
    help = 'Crear los roles Admin y Usuario con permisos'

    def handle(self, *args, **kwargs):
        # Crear roles (grupos)
        admin_group, created = Group.objects.get_or_create(name='Admin')
        user_group, created = Group.objects.get_or_create(name='Usuario')

        # Crear permisos
        content_type = ContentType.objects.get_for_model(Tarea)

        # Permisos para el Admin
        add_permission = Permission.objects.create(
            codename='can_add_tarea',
            name='Can add tarea',
            content_type=content_type
        )
        edit_permission = Permission.objects.create(
            codename='can_edit_tarea',
            name='Can edit tarea',
            content_type=content_type
        )

        # Asignar permisos al grupo Admin
        admin_group.permissions.add(add_permission, edit_permission)

        # Permisos para el Usuario
        view_permission = Permission.objects.create(
            codename='can_view_tarea',
            name='Can view tarea',
            content_type=content_type
        )

        # Asignar solo el permiso de ver tareas al grupo Usuario
        user_group.permissions.add(view_permission)

        # Mensaje de éxito
        self.stdout.write(self.style.SUCCESS('Roles y permisos creados y asignados correctamente'))