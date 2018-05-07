from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Intro


def index(request):
	intro= Intro.objects.all()
	return render_to_response('about.html',locals())
