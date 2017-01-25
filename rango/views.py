from django.shortcuts import render

from django.http import HttpResponse #import the HttpResponse object from the django.http module

def index(request): #Each view takes in at least one argument - a HttpRequest object (lives in django.http module). Named request by convention. 
	return HttpResponse("Rango says hey there partner!") #each view must return a HttpResponse object
	#A simple HttpResponse object takes a string parameter representing the content of the page we wish to send to the client requesting the view