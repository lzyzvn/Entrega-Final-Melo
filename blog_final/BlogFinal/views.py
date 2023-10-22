from django.shortcuts import render
from BlogFinal.forms import LoginFormulario
from models import Usuario, Blogs
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def inicio(request):
    return render(request,'BlogFinal/index.html')
def login(request):
    if request.method== "POST":
        miformulario= LoginFormulario(request.POST)
        print (miformulario)

        if miformulario.is_valid:
            informacion= miformulario.cleaned_data
            usuario= Usuario(nombre=informacion["nombre"],contraseña=informacion["contraseña"])
            usuario.save()
            return render (request,'BlogFinal/index.html')
        else:
            miformulario= LoginFormulario()
        return render (request,'BlogFinal/login.html',{"mi formulario":miformulario})
    

def leerUsuario(request):
    usuarios=Usuario.objects.all()
    contexto={"usuarios":usuarios}
    return render(request,'BlogFinal/leerUsuarios.html',contexto)


def EliminarUsuario(request,nombreusuario):
    usuario=Usuario.objects.get(nombre=nombreusuario)
    usuario.delete()
    usuarios=Usuario.objects.all()
    contexto={"usuarios":usuarios}
    return render(request,'BlogFinal/leerusuarios.html',contexto)

def editarUsuario(request,usuario_nombre):
    usuario=LoginFormulario.objects.get(nombre=usuario_nombre)
    if request.method=="POST":
        miFormulario= LoginFormulario(request.POST)
        informacion=miFormulario.cleaned_data
        usuario.nombre=informacion['nombre']
        usuario.contraseña=informacion['contraseña']
        usuario.email=informacion['email']
        usuario.save()
        return render(request, "BlogFinal/index.html")
    else:
        miFormulario= LoginFormulario(initial={'nomre':usuario.nombre,'apellido':usuario.contraseña,'email':usuario.email})

    return render(request,'BlogFinal/LeerUsuarios.html',{'miFormulario':miFormulario,'usuario_nombre':usuario_nombre})

        
def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contraseña=form.cleaned_data.get('password')
            user=authenticate(username=usuario,password=contraseña)
            if user is not None:
                login(request,user)
                return render(request,'BlogFinal/index.html',{"mensaje":f"bienvenido{usuario}"})
            else:
                return render(request,'BlogFinal/index.html',{"mensaje":"error, datos incorrectos"})
        else:
            return render(request,'BlogFinal/index.html',{"mensaje":"error, formulario erroneo"})
    form=AuthenticationForm()
    return render(request,'BlogFinal/login.html',{'form':form})


def register(request):
    if request.method=="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,'BlogFinal/inicio.html',{"mensaje":"usuario Creado"})
        
    else:
        form=UserCreationForm()

    return render(request,'BlogFinal/inicio.html',{"form",form})
def leerBlogs(request):
    blogs=Blogs.objects.all()
    contexto={"blogs":blogs}
    return render(request,'BlogFinal/blogs.html',contexto)
    
