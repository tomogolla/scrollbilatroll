
from django.shortcuts import render

# Homepage view
def homepage(request):
	return render(request, "homepage.html")


def about_view(request):
	return render(request, 'about.html')