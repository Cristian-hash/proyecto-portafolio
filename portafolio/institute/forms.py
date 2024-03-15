from django import forms
from django.contrib.auth.models import Group
from .models import Course, User
from captcha.fields import CaptchaField, CaptchaTextInput

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['names','first_last_name','second_last_name','age','dni', 'groups']
    
    names = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'input_field', 'placeholder':'Nombre', 'id':'names_input', 'data-error':'Tiene que añadir un nombre'}))
    first_last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'input_field', 'placeholder':'Primer Apellido', 'id':'first_last_name_input', 'data-error':'Tiene que añadir un Apellido'}))
    second_last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'input_field', 'placeholder':'Segundo Apellido', 'id':'second_last_name_input', 'data-error':'Tiene que añadir un Apellido'}))
    age = forms.IntegerField(label='', min_value=0, max_value=99, widget=forms.NumberInput(attrs={'class':'input_field', 'placeholder':'Edad', 'id':'age_input', 'data-error':'Tiene que añadir su edad', 'name':'age'}))
    dni = forms.IntegerField(label='', min_value=0, max_value=99999999, widget=forms.NumberInput(attrs={'class':'input_field', 'placeholder':'DNI', 'id':'dni_input', 'data-error':'Tiene que añadir su número de DNI'}))
    GROUP_CHOICES = [(group.id, group.name) for group in Group.objects.filter(name__in=['Alumno', 'Profesor'])]
    groups = forms.ChoiceField(label='Rol', choices=GROUP_CHOICES, widget=forms.RadioSelect)
    #group = forms.ModelChoiceField(queryset=Group.objects.filter(name__in=['Alumno', 'Profesor']), required=True)

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['names','first_last_name','second_last_name']
    
    names = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'input_field', 'placeholder':'Nombre', 'id':'names_input', 'data-error':'Tiene que añadir un nombre' }))
    first_last_name = forms.CharField(label='Primer apellido', widget=forms.TextInput(attrs={'class':'input_field', 'placeholder':'Primer Apellido', 'id':'first_last_name_input', 'data-error':'Tiene que añadir un Apellido'}))
    second_last_name = forms.CharField(label='Segundo apellido', widget=forms.TextInput(attrs={'class':'input_field', 'placeholder':'Segundo Apellido', 'id':'second_last_name_input', 'data-error':'Tiene que añadir un Apellido'}))

class LoginForm(forms.Form):
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'class':'input_field', 'placeholder':'Email', 'id':'email_input', 'data-error':'Debe ingresar un correo'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'input_field', 'placeholder':'Contraseña', 'id':'password_input', 'data-error':'Debe ingresar una contraseña'}))
    #captcha = CaptchaField(label='', error_messages={'invalid': "Verification code error"}, widget=CaptchaTextInput(attrs={'class':'input_field', 'placeholder':'Ingrese el Captcha', 'data-error':'Tiene que ingresar el Captcha'}))

                                                 
class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name','teoric_hours','practice_hours','credits']

    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'input_field', 'id':'names_input', 'placeholder':'Nombre Curso', 'data-error':'Tiene que añadir un nombre' }))
    teoric_hours = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class':'input_field', 'id':'teoric_hours_input', 'placeholder':'Horas Teoricas', 'data-error':'Tiene que añadir cantidad de Horas Teoricas'}))
    practice_hours = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class':'input_field', 'id':'practice_hours_name_input', 'placeholder':'Horas Practicas', 'data-error':'Tiene que añadir cantidad de Horas Practicas'}))
    credits = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class':'input_field', 'id':'credits_input', 'placeholder':'Creditos', 'data-error':'Tiene que añadir cantidad de Creditos'}))


class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name','teoric_hours','practice_hours','credits']

    name = forms.CharField(label='Nombre del Curso', widget=forms.TextInput(attrs={'class':'input_field', 'id':'names_input', 'placeholder':'Nombre Curso', 'data-error':'Tiene que añadir un nombre' }))
    teoric_hours = forms.IntegerField(label='Horas Teóricas', widget=forms.NumberInput(attrs={'class':'input_field', 'id':'teoric_hours_input', 'placeholder':'Horas Teoricas', 'data-error':'Tiene que añadir cantidad de Horas Teoricas'}))
    practice_hours = forms.IntegerField(label='Horas Prácticas', widget=forms.NumberInput(attrs={'class':'input_field', 'id':'practice_hours_name_input', 'placeholder':'Horas Practicas', 'data-error':'Tiene que añadir cantidad de Horas Practicas'}))
    credits = forms.IntegerField(label='Créditos', widget=forms.NumberInput(attrs={'class':'input_field', 'id':'credits_input', 'placeholder':'Creditos', 'data-error':'Tiene que añadir cantidad de Creditos'}))
