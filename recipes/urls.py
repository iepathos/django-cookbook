from django.conf.urls.defaults import patterns, include, url

from recipes.views import RecipeDetailView, RecipeListView, RecipePDFView

from recipes.api import RecipeResource
recipe_resource = RecipeResource()


urlpatterns = patterns('recipes.views',
    url(r'^add/$', 'add', name='recipes_recipe_add'),
    url(r'^edit/(?P<recipe_id>\d+)/$', 'edit', name='recipes_recipe_edit'),
)

urlpatterns += patterns('',
	url(r'^recipes/(?P<slug>[-\w]+)/$', RecipeDetailView.as_view(),
		name='recipes_recipe_detail'),
	url(r'^recipes/(?P<slug>[-\w]+)/pdf/$', RecipePDFView.as_view(),
		name='recipes_recipe_detail_pdf'),
	url(r'^$', RecipeListView.as_view(), name='recipes_recipe_index'),
)

urlpatterns += patterns('',
	url(r'^api/', include(recipe_resource.urls)),
)
