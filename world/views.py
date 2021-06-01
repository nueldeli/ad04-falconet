from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class WorldHomeView(TemplateView):
	template_name = 'world/world_home.html'