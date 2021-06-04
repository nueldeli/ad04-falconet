from django.shortcuts import render
from .models import Post
#from django.views.generic import TemplateView

# Create your views here.
def world_view(request):
	return render(request, 'world/world_home.html')

def search_location(request):
	if request.method == "POST":
		searched = request.POST.get('searched')
		locations = Post.objects.filter(coordinate__contains=searched)
		return render(request, 'world/search_location.html', {'searched':searched, 'locations':locations})
	else:
		return render(request, 'world/search_location.html', {})