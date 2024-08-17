from django.shortcuts import render, redirect
from .models import Equipo, Arriendo, Usuario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request,'index.html')


def crear_user(request):
    if request.method == 'GET':
        return render(request, 'crear_user.html')
    else:
        user = User.objects.create_user(
            username = request.POST['username'],
            password= request.POST['password']
        )
        Usuario.objects.create(
            user=user,
            name = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password'],
            tipo = request.POST['tipo_usuario']
        )
        return render(request, 'crear_user.html')


@login_required
def listar_productos(request):
    if request.method == 'GET':
        equipos = Equipo.objects.filter(estado = 'Disponible')
        context = {
        'equipos' : equipos
        }
        return render(request,'listar_productos.html', context)
    else:
        equipos = Equipo.objects.filter(categoria=request.POST['categoria'], estado = 'Disponible')
        context = {
        'equipos' : equipos
        }
        return render(request,'listar_productos.html', context)


@login_required
def arrendar(request,id):
    if request.method == 'GET':
        equipo = Equipo.objects.get(id=id)
        return render(request, 'arrendar.html',{'equipo':equipo})
    else:
        equipo = Equipo.objects.filter(id = request.POST['id'])
        equipo_2 = Equipo.objects.get(id=id)
        equipo.update(estado='Arrendado')
        Arriendo.objects.create(
            usuario = Usuario.objects.get(user=request.user),
            equipo= equipo_2,
        )
        return render(request, 'arrendar.html',{'equipo':equipo_2})
    

def listar_arriendos(request):
    if request.method == 'GET':
        usuario = Usuario.objects.get(user = request.user)
        if usuario.tipo == 'Operario':
            arriendos = Arriendo.objects.all()
            return render(request, 'listar_arriendos.html',{'arriendos':arriendos})
        else:
            return redirect('listar_productos')
    else:
        arriendo = Arriendo.objects.filter(id=request.POST['id'])
        arriendo.update(observacion=request.POST['observacion'])
        arriendos = Arriendo.objects.all()
        return render(request, 'listar_arriendos.html',{'arriendos':arriendos})
