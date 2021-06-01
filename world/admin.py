from django.contrib import admin
from .models import Post, Coordinate

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('coordinate', 'author')

class CoordinateAdmin(admin.ModelAdmin):
	list_display = ('lat', 'lon')

admin.site.register(Post, PostAdmin)
admin.site.register(Coordinate, CoordinateAdmin)