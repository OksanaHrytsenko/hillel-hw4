from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models
from .models import Teachers


def get_teachers(request):
    all_teachers = Teachers.objects.all().values()
    template = loader.get_template('teacher_list.html')
    context = {'teachers': all_teachers}
    return HttpResponse(template.render(context, request))
