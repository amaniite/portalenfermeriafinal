from django.shortcuts import render, redirect, get_list_or_404
from .models import Profesional 
from .forms import CustomEnfermeraForm, ProfesionalForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as login1, authenticate

# Create your views here.

def home(request):
    profesionales = Profesional.objects.all()
    data = {
        'profesionales':profesionales
    }
    return render (request, "core/home.html", data)

def search(request):
    template_name = "core/home.html"
    busqueda = request.GET["busqueda"]
    profesionales = Profesional.objects.filter(comuna__nombre__icontains=busqueda)
    data = {
        'profesionales':profesionales
    }
    return render(request, template_name, data)
    

@login_required
def registroDatosEU(request):
    data = {
        'form': ProfesionalForm()
    }

    if request.method == 'POST':
        formulario = ProfesionalForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
        else:
            data['form'] = formulario
    return render (request, "registration/datosenfermera.html", data)

def profesionalDetailsView(request, pk):

    profesional = Profesional.objects.get(pk=pk)

    return render (request, "core/profesional_detalle.html", {'profesional': profesional})

def contacto(request):
    return render (request, "core/contacto.html")
                   
def registroEU(request):
    data = {
        'form':CustomEnfermeraForm()
    }
    if request.method == 'POST':
        formulario = CustomEnfermeraForm(data=request.POST)
        
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login1(request, user)
            return redirect('datosenfermera')
    return render (request, "registration/registroenfermera.html", data)

def modificardatos(request, user):

    profesional = Profesional.objects.get(user__username=user)

    data = {
        'form': ProfesionalForm(instance=profesional)
    }
    
    if request.method == 'POST':
        formulario = ProfesionalForm(data=request.POST, instance=profesional)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
        else:
            data['form'] = formulario
    return render(request,"registration/modificardatos.html", data)