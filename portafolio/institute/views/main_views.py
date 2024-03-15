from django.shortcuts import render
from django.views.generic import TemplateView
from ..models import Course

def index(request):
    context = {
        'popular_courses': Course.objects.filter(is_popular = True)
    }
    return render(request, 'index.html', context)