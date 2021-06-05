from django.shortcuts import render
from .models import Post
from .forms import AddPostForm
from django.views.generic import TemplateView, CreateView

# Create your views here.
#def world_view(request):
	#django_variable = Post.objects.all()
	#return render(request, 'world/world_home.html', {'django_variable':django_variable})

#def search_location(request):
	#if request.method == "POST":
		#searched = request.POST.get('searched')
		#locations = Post.objects.filter(coordinate__contains=searched)
		#return render(request, 'world/search_location.html', {'searched':searched, 'locations':locations})
	#else:
		#return render(request, 'world/search_location.html', {})

class HomeView(TemplateView):
	template_name = 'world/post_home.html'

class AddPostView(CreateView):
	model = Post
	form_class = AddPostForm
	template_name = 'world/post_add.html'