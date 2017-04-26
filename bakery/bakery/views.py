from django.shortcuts import render

from django.http import HttpResponse

# developed by @raphaeltataia

def index(request):
	return HttpResponse("What's up?!")
