from django import forms
from .models import Animal, Personal, Evento
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'
        
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'   