# Importa la configuración del proyecto Django. Se usa aquí para acceder al modelo de usuario.
from django.conf import settings
# Importa la funcionalidad de modelos de Django, que es la base para definir tus tablas de base de datos.
from django.db import models
# Importa herramientas de tiempo y zona horaria de Django. Es mejor usar esto que el módulo 'datetime' estándar de Python
# para manejar las zonas horarias correctamente.
from django.utils import timezone

#DANDO ATRIBUTOS A LA CLASE
# Define el modelo 'Post'. models.Model indica que esta clase es un modelo de Django y se 
# mapeará a una tabla en la base de datos.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
#esta linea de arriba permite  quela fecha no sea un campo oblogatorio es decir que pueda estar vacio
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title