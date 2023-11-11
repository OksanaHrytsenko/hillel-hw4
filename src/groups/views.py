from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . import models
from .models import Groups


def get_groups(request):
    all_groups = Groups.objects.all().values()
    template = loader.get_template('group_list.html')
    context = {'groups': all_groups}

    return HttpResponse(template.render(context, request))
