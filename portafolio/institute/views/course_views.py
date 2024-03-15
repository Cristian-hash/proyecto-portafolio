from django.shortcuts import render, redirect
from ..models import Course
#Colocar forms para cursos
from django.contrib import messages
from ..forms import CreateCourseForm, EditCourseForm
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


class CourseCreateView(PermissionRequiredMixin, CreateView):
    model = Course
    form_class = CreateCourseForm
    template_name = 'addCourse.html'
    success_url = reverse_lazy('view_courses')
    permission_required = 'institute.view_course'
    permission_denied_message = 'Usted no puede agregar cursos porque no tiene los permisos necesarios'

    def post(self, request):
        form = CreateCourseForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            teoric_hours = form.cleaned_data.get('teoric_hours')
            practice_hours = form.cleaned_data.get('practice_hours')
            credits = form.cleaned_data.get('credits')
            
            new_course = Course(
                name = name,
                teoric_hours = teoric_hours,
                practice_hours = practice_hours,
                credits = credits,
            )

            new_course.save()

            messages.success(request, f'Se creó el curso {name}') 
            return redirect('view_courses')
        else:
            messages.error(request,'Hubo algún error')           
            return redirect('add_course')


class CourseListView(PermissionRequiredMixin, ListView):
    model = Course
    template_name = 'viewCourses.html'
    queryset = Course.objects.filter(is_popular = False)
    context_object_name = 'courses'
    permission_required = 'institute.view_course'
    permission_denied_message = 'Usted no puede ver el listado de cursos porque no tiene los permisos necesarios'

class CourseUpdateView(PermissionRequiredMixin, UpdateView):
    model = Course
    form_class = EditCourseForm
    template_name = 'editCourse.html'
    success_url = reverse_lazy('view_courses')
    permission_required = 'institute.change_course'
    permission_denied_message = 'Usted no puede editar la información de un curso porque no tiene los permisos necesarios'

class CourseDeleteView(PermissionRequiredMixin, DeleteView):
    model = Course
    template_name = 'deleteCourse.html'
    success_url = reverse_lazy('view_courses')
    permission_required = 'institute.delete_course'
    permission_denied_message = 'Usted no puede eliminar ningun curso porque no tiene los permisos necesarios'


