
from django.urls import path
from . import views

urlpatterns = [
	path("", views.homepage, name="home"),
    path('about', views.about_view, name='about'),
    path('digital-villlage', views.digital_village, name='digital-village'),
    path('contact', views.contact_view, name='contact'),
    path('advocacy', views.advocacy_view, name='advocacy'),
    path('resources', views.resources_view, name='resources'),
    path('events', views.events_view, name='events'),
]
