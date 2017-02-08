from django.shortcuts import render

from django.http import HttpResponse #import the HttpResponse object from the django.http module

#Each view takes in at least one argument - a HttpRequest object (lives in django.http module). Named request by convention.
#Each view must return a HttpResponse object
#A simple HttpResponse object takes a string parameter representing the content of the page we wish to send to the client requesting the view


def index(request):
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"} # Construct a dictionary to pass to the template engine as its context. Note the key boldmessage is the same as {{ boldmessage }} in the template!
	return render(request, 'rango/index.html', context=context_dict)
	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier. Note that the first parameter is the template we wish to use.


def about(request):
	return render(request, 'rango/about.html', context={})
