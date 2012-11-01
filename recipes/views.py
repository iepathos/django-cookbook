from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView, ListView

from cookbook.views import PDFView

# Data models and forms
from recipes.models import Recipe
from recipes.forms import RecipeForm

# Logging
import logging
logger = logging.getLogger(__name__)

class RecipePDFView(PDFView):
	model = Recipe
	template_name = 'recipes/detail_pdf.html'
		

class RecipeListView(ListView):
	template_name = 'recipes/index.html'
	
	def get_queryset(self):
		recipes = Recipe.active.all()
		logger.debug('Number of Recipes: %d' % recipes.count())
		return recipes
		
class RecipeDetailView(DetailView):
	queryset = Recipe.active.all()
	template_name = 'recipes/detail.html'


def detail(request, slug):
	recipe = get_object_or_404(Recipe, slug=slug)
	return render(request, 'recipes/detail.html', 
		{'object': recipe})
		
@login_required
def add(request):
	if request.method == 'POST':
		form = RecipeForm(user=request.user, data=request.POST)
		if form.is_valid():
			recipe=form.save()
			return HttpResponseRedirect(recipe.get_absolute_url())
	else:
		form = RecipeForm()
	return render(request, 'recipes/form.html',
		{'form': form, 'add': True})

@login_required
def edit(request, recipe_id):
	recipe = get_object_or_404(Recipe, pk=recipe_id)
	if recipe.author != request.user and not request.user.is_staff:
		return HttpResponseForbidden()
	if request.method == 'POST':
		form = RecipeForm(instance=recipe, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(recipe.get_absolute_url())
	else:
		form = RecipeForm(instance=recipe)
	return render(request, 'recipes/form.html',
		{'form': form, 'add': False, 'object': recipe})
