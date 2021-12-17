from django.shortcuts import render

from apps.post.models import categoria, post

def EcoGreen(request):

	r = categoria.objects.all()

	ctx = {}
	ctx['categorias'] = r

	
	return render(request,'EcoGreen.html',ctx)
    
    

