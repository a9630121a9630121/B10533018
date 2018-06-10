from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def article(request):
	if request.method == 'POST':
		print(request.POST.get('pk'))
		try:
			primarykey = request.POST.get('pk')
			Articles.objects.get(pk=primarykey).delete()
		except Exception as e:
			pass
	article=Articles.objects.all()
	return render(request, 'article.html',{'article':article})

def create(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		text = request.POST.get('content')
		Articles.objects.create(title=title, text=text)
		return redirect('/blog')
	return render(request, 'create.html')

def edit(request):
	pk = request.GET.get('q')
	article = Articles.objects.get(pk=pk)
	if request.method == 'POST':
		article.title = request.POST.get('title')
		article.content = request.POST.get('content')
		article.save()
		return redirect('/blog')
	return render(request, 'edit.html', {'article': article})
