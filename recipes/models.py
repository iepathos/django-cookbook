# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Category(models.Model):
	"""Category model."""
	name = models.CharField(u'Name', max_length=100)
	slug = models.SlugField(unique=True)
	description = models.TextField(u'Description', blank=True)

	class Meta:
		verbose_name = u'Category'
		verbose_name_plural = u'Categories'
		
	def __unicode__(self):
		return self.name

class ActiveRecipeManager(models.Manager):
	def get_query_set(self):
		return super(ActiveRecipeManager, self).get_query_set().filter(is_active=True)

class Recipe(models.Model):
	""" Recipe model. """
	is_active = models.BooleanField(u'Active')
	
	objects = models.Manager()
	active = ActiveRecipeManager()
	
	def get_related_recipes(self):
		categories = self.category.all()
		related_recipes = Recipe.active.all().filter(
			difficulty_exact=self.difficulty, category_in=categories)
		return related_recipes.exclude(pk=self.id).distinct()
	
	DIFFICULTY_EASY = 1
	DIFFICULTY_MEDIUM = 2
	DIFFICULTY_HARD = 3
	DIFFICULTIES = (
		(DIFFICULTY_EASY, u'easy'),
		(DIFFICULTY_MEDIUM, u'normal'),
		(DIFFICULTY_HARD, u'hard'),
	)
	title = models.CharField(u'Title', max_length=255)
	slug = models.SlugField(unique=True)
	ingredients = models.TextField(u'Ingredients',
		help_text = u'One ingredient per line')
	preparation = models.TextField(u'Preparation')
	time_for_preparation = models.IntegerField(u'Preparation Time',
		help_text = u'Specify time in minutes', blank=True, null=True)
	number_of_portions = models.PositiveIntegerField(u'Number of Portions')
	difficulty = models.SmallIntegerField(u'Difficulty',
		choices=DIFFICULTIES, default=DIFFICULTY_MEDIUM)
	category = models.ManyToManyField(Category, verbose_name=u'Categories')
	author = models.ForeignKey(User, verbose_name=u'Authors')
	date_created = models.DateTimeField(editable=False)
	date_updated = models.DateTimeField(editable=False)
	
	class Meta:
		verbose_name = u'Recipe'
		verbose_name_plural = u'Recipes'
		ordering = ['-date_created']
		
	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.id:
			self.date_created = now()
		self.date_updated = now()
		super(Recipe, self).save(*args, **kwargs)
		
	@models.permalink
	def get_absolute_url(self):
		return ('recipes_recipe_detail', (), { 'slug': self.slug })
