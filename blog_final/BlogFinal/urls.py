from django.urls import path
from BlogFinal.views import inicio, leerUsuario,EliminarUsuario,editarUsuario,login_request,register,logout
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('inicio', inicio),
    path('usuarios', leerUsuario),
    path('eliminar usuario/nombreusuario/', EliminarUsuario,name='eliminarusuario'),
    path('editar usuario/nombreusuario/', editarUsuario,name='editarusuario'),
    path('login', login_request,name='login'),
    path('register', register,name='register'),
    path('logout', LogoutView.as_view(template_name='BlogFinal/logout.html'),name='logout'),

    
   
]