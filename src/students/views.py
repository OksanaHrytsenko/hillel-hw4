from random import random, choice

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


from . import models
from .models import Students


def get_students(request):
    all_students = Students.objects.all().values()
    template = loader.get_template('student_list.html')
    context = {'students': all_students}

    return HttpResponse(template.render(context, request))



