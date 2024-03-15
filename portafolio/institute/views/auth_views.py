from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from ..models import User
from ..forms import LoginForm
from django.contrib import messages

#Método para el login
def login(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(email = email, password = password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'El email o la contraseña no son correctos')
                return redirect('login')
        else:
            messages.error(request,'Captcha Incorrecto') 
            return redirect('login')
    elif request.user.is_authenticated:
        return redirect('/')
    else:
        context = {
	        'form':form,
	    }  
        return render(request, 'login.html', context)

def register(request):
    if request.method == 'POST':
        #roles_id = Role.objects.all()
        names = request.POST['names']
        first_last_name = request.POST['first_last_name']
        second_last_name = request.POST['second_last_name']
        email = request.POST['email']
        password_1 = request.POST['password_1']
        password_2 = request.POST['password_2']

        if email.split('@')[1] == 'imc.edu.pe':
            messages.error(request, 'No tiene permiso para registrarse con el dominio de la institución')
            return redirect('register')
        elif password_1 == password_2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Este correo ya está registrado')
                return redirect('register')
            else:
                new_user = User(
                    names = names,
                    first_last_name = first_last_name,
                    second_last_name = second_last_name,
                    email = email,
                    #role = Role.objects.get(pk=1)
                )
                new_user.set_password(password_1)
                new_user.save()
                return redirect('login')
        else:
            messages.info(request, 'Las contraseñas no coinciden')
            return redirect('register')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'Salio de la sesión') 
    return redirect('/')