from django.urls import path
from .views import world_view, search_location

urlpatterns = [
	path('', world_view, name='world_view'),
	path('search_location/', search_location, name='search_location'),
]