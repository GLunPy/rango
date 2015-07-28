from django.shortcuts import HttpResponse
from django.shortcuts import render

def index(request):
	context_dict = {'boldmessage': "Soy un mensaje en negrita"}
	return render(request, 'rango/index.html',context_dict)
# Create your views here.
