from django.http import HttpResponse
# from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def brag(request):
    return HttpResponse('My braggable Apps so far')