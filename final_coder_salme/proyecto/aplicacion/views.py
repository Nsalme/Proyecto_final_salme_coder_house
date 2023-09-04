from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal, Personal, Evento
from .forms import AnimalForm, EventoForm, PersonalForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required




def home(request):
    # Lógica para la página de inicio
    return render(request, 'aplicacion/home.html')
def home(request):
    # Lógica para la página de inicio
    return render(request, 'aplicacion/home.html')

def Sobre_mi(request):
    return render(request,'aplicacion/sobre_mi.html')


# Vista para iniciar sesión
def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Credenciales incorrectas. Intente de nuevo.')
        else:
            messages.error(request, 'Credenciales incorrectas. Intente de nuevo.')
    else:
        form = AuthenticationForm()
    return render(request, 'aplicacion/iniciar_sesion.html', {'form': form})

# Vista para cerrar sesión
def cerrar_sesion(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')
    return redirect('home')



def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'aplicacion/registro.html', {'form': form})

#######################################################################
@login_required(login_url='home')
def Sobre_mi(request):
    return render(request,'aplicacion/sobre_mi.html')

@login_required(login_url='home')
def animales(request):
    animales = Animal.objects.all()
    return render(request, 'aplicacion/animales.html', {'animales': animales})

@login_required(login_url='home')
def personal(request):
    personal = Personal.objects.all()
    return render(request, 'aplicacion/personal.html', {'personal': personal})

@login_required(login_url='home')
def formularios(request):
    return render(request, 'aplicacion/formularios.html')


# SE CREAN  OBJETOS

def lista_animales(request):
    # Recupera todos los objetos Animal de la base de datos
    animales = Animal.objects.all()
    return render(request, 'aplicacion/animales.html', {'animales': animales})

def agregar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('animales')
    else:
        form = AnimalForm()
    
    return render(request, 'aplicacion/agregar_animal.html', {'form': form})

def agregar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('evento')
    else:
        form = EventoForm()
    
    return render(request, 'aplicacion/agregar_evento.html', {'form': form})

def agregar_personal(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('personal') 
    else:
        form = PersonalForm()

    return render(request, 'aplicacion/agregar_personal.html', {'form': form})


#vista detalle
def detalle_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'aplicacion/detalle_animal.html', {'animal': animal})

def detalle_personal(request, personal_id):
    personal = get_object_or_404(Personal, pk=personal_id)
    return render(request, 'aplicacion/detalle_personal.html', {'personal': personal})


def detalle_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'aplicacion/detalle_evento.html', {'evento': evento})
def evento(request):
    evento = Evento.objects.all()
    return render(request, 'aplicacion/evento.html', {'evento': evento})


def evento(request):
    eventos = Evento.objects.all()
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('evento')
    else:
        form = EventoForm()

    return render(request, 'aplicacion/evento.html', {'evento': eventos, 'form': form})




####### CRUD DE CLASES 
# Vista base para las vistas CRUD
class BaseCRUDView(View):
    template_name = None
    form_class = None
    model = None
    redirect_url = None

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        objects = self.model.objects.all()
        return render(request, self.template_name, {'form': form, 'objects': objects})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(self.redirect_url)
        objects = self.model.objects.all()
        return render(request, self.template_name, {'form': form, 'objects': objects})

# Vistas CRUD para Personal
class PersonalListView(ListView):
    model = Personal
    template_name = 'aplicacion/lista_personal.html'
    context_object_name = 'personal'

class PersonalDetailView(DetailView):
    model = Personal
    template_name = 'aplicacion/detalle_personal.html'
    context_object_name = 'persona'

class PersonalCreateView(CreateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'aplicacion/crear_personal.html'
    success_url = reverse_lazy('lista_personal')

class PersonalUpdateView(UpdateView):
    model = Personal
    form_class = PersonalForm
    template_name = 'aplicacion/editar_personal.html'
    success_url = reverse_lazy('lista_personal')

class PersonalDeleteView(DeleteView):
    model = Personal
    template_name = 'aplicacion/eliminar_personal.html'
    success_url = reverse_lazy('lista_personal')

    ### cbv animales

    
# Vista para listar todos los animales
class AnimalListView(ListView):
    model = Animal
    template_name = 'aplicacion/lista_animales.html'
    context_object_name = 'animales'

# Vista para ver los detalles de un animal específico
class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'aplicacion/detalle_animal.html'
    context_object_name = 'animal'

# Vista para crear un nuevo animal
class AnimalCreateView(CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'aplicacion/crear_animal.html'
    success_url = reverse_lazy('lista_animales')

# Vista para actualizar la información de un animal
class AnimalUpdateView(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'aplicacion/editar_animal.html'
    success_url = reverse_lazy('lista_animales')

# Vista para eliminar un animal
class AnimalDeleteView(DeleteView):
    model = Animal
    template_name = 'aplicacion/eliminar_animal.html'
    success_url = reverse_lazy('lista_animales')


    ### crud de eventos
    # Lista de eventos
class EventoListView(ListView):
    model = Evento
    template_name = 'aplicacion/evento_list.html'
    context_object_name = 'eventos'

# Detalle de un evento
class EventoDetailView(DetailView):
    model = Evento
    template_name = 'aplicacion/evento_detail.html'
    context_object_name = 'evento'

# Crear un nuevo evento
class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'aplicacion/evento_form.html'
    success_url = reverse_lazy('evento_list')

# Actualizar un evento existente
class EventoUpdateView(UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'aplicacion/evento_form.html'
    context_object_name = 'evento'
    success_url = reverse_lazy('evento_list')

# Eliminar un evento existente
class EventoDeleteView(DeleteView):
    model = Evento
    template_name = 'aplicacion/evento_confirm_delete.html'
    context_object_name = 'evento'
    success_url = reverse_lazy('evento_list')
