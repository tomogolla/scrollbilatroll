
from django.shortcuts import render

# Homepage view
def homepage(request):
	return render(request, "homepage.html")


def about_view(request):
	return render(request, 'about.html')

def digital_village(request):
	return render(request, 'digitalvillage.html')

def contact_view(request):
	return render(request, 'contact.html')

def advocacy_view(request):
	return render(request, 'comming_soon.html')

def resources_view(request):
	return render(request, 'comming_soon.html')
def events_view(request):
	return render(request, 'comming_soon.html')