# api.py for recipes and RESTful web service
from tastypie.resources import ModelResource

from recipes.models import Recipe

class RecipeResource(ModelResource):
	class meta:
		queryset = Recipe.objects.all()
		resource_name  = 'recipe'
