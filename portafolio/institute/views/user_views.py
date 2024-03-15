from django.http import HttpResponseForbidden
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
from ..models import User
from ..forms import CreateUserForm, EditUserForm
from django.urls import reverse_lazy
from django.contrib import messages
import random

from django.http import HttpResponse
from django.template.loader import render_to_string

def create_institutional_email(names, first_last_name, second_last_name):
    first_last_name_whitout_spaces = first_last_name.replace(' ','')
    email = names[0] + first_last_name_whitout_spaces + second_last_name[0]
    email = email.lower() + '@imc.edu.pe'
    extra_number = 1
    while User.objects.filter(email = email).exists():
        if extra_number > 1:
            email = email.replace(f'{extra_number-1}@', f'{extra_number}@')
        else:
            email = email.replace('@', f'{extra_number}@')
        extra_number += 1
    return email

def create_random_password():
    password=''
    for i in range(8):
        password +=str(random.randint(0,9))
    return password

class UserCreateView(PermissionRequiredMixin, CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'addUser.html'
    success_url = reverse_lazy('view_users')
    permission_required = 'institute.view_user'
    permission_denied_message = 'Usted no puede agregar usuarios porque no tiene los permisos necesarios'

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            names = form.cleaned_data.get('names')
            first_last_name = form.cleaned_data.get('first_last_name')
            second_last_name = form.cleaned_data.get('second_last_name')
            age = form.cleaned_data.get('age')
            dni = form.cleaned_data.get('dni')
            group_id = form.cleaned_data.get('groups')
            group = Group.objects.get(pk=group_id)   
            email = create_institutional_email(names, first_last_name, second_last_name)
            password = create_random_password()
            
            new_user = User(
                names = names,
                first_last_name = first_last_name,
                second_last_name = second_last_name,
                age = age,
                dni = dni,
                email = email,
            )
            new_user.set_password(password)
            new_user.save()
            new_user.groups.add(group)
            new_user.save()

            messages.success(request, f'Se creó el usuario con el correo {email} y la contraseña {password}') 
            return redirect('view_users')
        else:
            messages.error(request,'Hubo algún error')           
            return redirect('add_user')

class UserListView(PermissionRequiredMixin, ListView):
    model = User
    template_name = 'viewUsers.html'
    queryset = User.objects.filter(is_superuser = False)
    context_object_name = 'users'
    permission_required = 'institute.view_user'
    permission_denied_message = 'Usted no puede ver el listado de usuarios porque no tiene los permisos necesarios'

class UserUpdateView(PermissionRequiredMixin, UpdateView):
    model = User
    form_class = EditUserForm
    template_name = 'editUser.html'
    success_url = reverse_lazy('view_users')
    permission_required = 'institute.change_user'
    permission_denied_message = 'Usted no puede editar la información de algún usuario porque no tiene los permisos necesarios'
    

class UserDeleteView(PermissionRequiredMixin, DeleteView):
    model = User
    template_name = 'deleteUser.html'
    success_url = reverse_lazy('view_users')
    permission_required = 'institute.delete_user'
    permission_denied_message = 'Usted no puede eliminar a ningún usuario porque no tiene los permisos necesarios'
    