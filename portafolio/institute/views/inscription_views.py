from django.shortcuts import render,redirect, get_object_or_404
from ..models import Inscription, User, Course
from datetime import date
#Formularios de matrículas
from django.contrib import messages

#Añadir matrícula
def add_inscription(request):
    if request.method == 'POST':
        email = request.POST['email']
        #Falta verificar si no se hizo una matrícula con ese correo
        user = User.objects.filter(email=email).first()
        print(user)
        courses = request.POST['courses']
        print('Cursos: ' + courses)
        year = date.today() #Corregir por el año actual según el sistema
        cycle = 1 #También corregir
        
        new_inscription = Inscription(
            user = user,
            year = year,
            cycle = cycle           
        )

        new_inscription.save()
        return redirect('add_inscription')
    else:
        courses = Course.objects.all()
        context = {
            'courses': courses
        }
        return render(request, 'addInscription.html', context)

#Ver matrículas
def view_inscriptions(request):
    inscriptions = Inscription.objects.all()
    context = {'inscriptions': inscriptions}
    return render(request, "viewInscriptions.html", context)

#Editar matrícula
def edit_inscription(request, id_Inscription):
    
    inscription = Inscription.objects.get(pk=id_Inscription)
    
    if request.method == 'POST':
        inscription.courses = request.POST['teoric_hours']

        inscription.save(update_fields=['courses'])

        return redirect('view_inscriptions')        

    else:
        context = {            
            'inscription': inscription,
        }    
        return render(request, "editInscription.html", context)

#Eliminar matrícula
def delete_inscription(request, id_Inscription):
    inscription = get_object_or_404(Inscription, id=id_Inscription)
    if request.method == 'POST':
        inscription.delete()
        return redirect('view_inscriptions') 
    context = {
        'inscription':inscription,
        'messageDelete': 'OK',
    }
    return render(request, 'deleteInscription.html', context)