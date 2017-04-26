from django.contrib import admin

# from .models import Recipe
# from .models import Chief
from models import *

# developed by @raphaeltataia

class RecipeAdmin(admin.ModelAdmin):
	list_display = ('chief', 'title', 'ingredients', 'way', 'created_date', 'published_date', 'people_served')

class ChiefAdmin(admin.ModelAdmin):
	list_display = ('cpf', 'name', 'city', 'state', 'email')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Chief, ChiefAdmin)