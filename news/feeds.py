from django.conf import settings
from django.contrib.syndication.views import Feed

from news.models import Article

class ArticleFeed(Feed):
	title = 'News from the Cookbook'
	link = '/'
	description = 'The RSS Feed from Cookbook website'
	
	def items(self):
		return Article.objects.order_by('-date_created')[:settings.NEWS_FEED_COUNT]
		
	def item_title(self, item):
		return item.headline
		
	def item_description(self, item):
		return item.body
