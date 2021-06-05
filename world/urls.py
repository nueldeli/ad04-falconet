from django.urls import path
from .views import HomeView, AddPostView

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('post_add/', AddPostView.as_view(), name='post_add')
	#path('search_location/', search_location, name='search_location'),
]