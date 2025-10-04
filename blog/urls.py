from django.urls import path
from . import views

#Aquí estamos importando la función de Django path y todos nuestras views desde la aplicación blog
#estamos asociando una vista (view) llamada post_list a la URL raíz
urlpatterns = [
    path('', views.post_list, name='post_list'),
]