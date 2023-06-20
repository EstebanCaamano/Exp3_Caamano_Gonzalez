from django.shortcuts import render, redirect
from plantitas.models import Producto
from .forms import ProductosForm, RegistroUserForm
from .models import Producto
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    return render(request,'inicio.html')


def pagina2(request):
    return render(request,'pagina2.html')

def formulario(request):
    return render(request,'formulario.html')


def api(request):
    return render(request,'api.html')


def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado Exitosamente []~(￣▽￣)~*")
            return redirect ('index')
        data["form"] = formulario
    return render(request, 'registration/registrar.html',data)




@login_required
def crear(request):
    if request.method=="POST":
        productosform = ProductosForm(request.POST, request.FILES)
        if productosform.is_valid():
            productosform.save()     #similar al insert
            return redirect('pagina3')
    else:
        productosform=ProductosForm()
    return render(request, 'crear.html', {'productosform':productosform})

@login_required
def eliminar(request, id):
    productoEliminado = Producto.objects.get(patente=id) #obtenemos un objeto por su id
    productoEliminado.delete()
    return redirect ('pagina3')


@login_required
def modificar(request, idproducto):
    producto = Producto.objects.get(id=idproducto)
    datos = {
        'form': ProductosForm(instance=producto)
    }
    if request.method=='POST':
        formulario = ProductosForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            instance = formulario.save(commit=False)
            if 'imagen' in request.FILES:
                instance.imagen = request.FILES['imagen']
                instance.save()
            return redirect('pagina3')
    return render(request, 'modificar.html', datos)





def tienda(request):
    productos = Producto.objects.all()
    data={
        'productos':productos
    }
    return render(request,'pagina3.html',data)


