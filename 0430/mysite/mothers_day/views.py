from django.shortcuts import render
from .models import *

def form(request):
	message=''
	if request.method=='POST':
		message = request.POST.get('message')
		Message.objects.create(message=message)
		return render(request,'form.html',{'message':message})
	return render(request,'form.html')

