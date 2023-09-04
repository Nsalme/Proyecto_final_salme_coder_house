from django.urls import path
from .views import*
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', home, name='home'),
    path('sobre_mi/', Sobre_mi, name='sobre_mi'),
    path('animales/', animales, name='animales'),
    path('personal/', personal, name='personal'),
    path('formularios/', formularios, name='formularios'),

    # Rutas para animales
    path('agregar_animal/', agregar_animal, name='agregar_animal'),
    path('detalle_animal/<int:animal_id>/', detalle_animal, name='detalle_animal'),

    # Rutas para eventos
    path('agregar_evento/', agregar_evento, name='agregar_evento'),
    path('detalle_evento/<int:evento_id>/', detalle_evento, name='detalle_evento'),

    # Rutas para personal
    path('agregar_personal/', agregar_personal, name='agregar_personal'),
    path('detalle_personal/<int:personal_id>/', detalle_personal, name='detalle_personal'),

    # Ruta para la lista de eventos
    path('evento/', evento, name='evento'),

    # Rutas para CRUD de Personal
    path('lista_personal/', PersonalListView.as_view(), name='lista_personal'),
    path('detalle_personal/<int:pk>/', PersonalDetailView.as_view(), name='detalle_personal_cbv'),
    path('crear_personal/', PersonalCreateView.as_view(), name='crear_personal_cbv'),
    path('editar_personal/<int:pk>/', PersonalUpdateView.as_view(), name='editar_personal_cbv'),
    path('eliminar_personal/<int:pk>/', PersonalDeleteView.as_view(), name='eliminar_personal_cbv'),

    # Rutas para CRUD de Animales
    path('lista_animales/', AnimalListView.as_view(), name='lista_animales'),
    path('detalle_animal/<int:pk>/', AnimalDetailView.as_view(), name='detalle_animal_cbv'),
    path('crear_animal/', AnimalCreateView.as_view(), name='crear_animal_cbv'),
    path('editar_animal/<int:pk>/', AnimalUpdateView.as_view(), name='editar_animal_cbv'),
    path('eliminar_animal/<int:pk>/', AnimalDeleteView.as_view(), name='eliminar_animal_cbv'),

    # Rutas para CRUD de Eventos
    path('lista_eventos/', EventoListView.as_view(), name='lista_eventos'),
    path('detalle_evento/<int:pk>/', EventoDetailView.as_view(), name='detalle_evento_cbv'),
    path('crear_evento/', EventoCreateView.as_view(), name='crear_evento_cbv'),
    path('editar_evento/<int:pk>/', EventoUpdateView.as_view(), name='editar_evento_cbv'),
    path('eliminar_evento/<int:pk>/', EventoDeleteView.as_view(), name='eliminar_evento_cbv'),

###inicio y cierre
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', registro, name='registro'),


]