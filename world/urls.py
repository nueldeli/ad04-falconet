from django.urls import path
from .views import WorldHomeView

urlpatterns = [
	path('', WorldHomeView.as_view(), name='world_home'),
]