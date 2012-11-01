# encoding: utf-8
from django.db import models

from cookbook.basemodels import DateTimeInfo

class Article(DateTimeInfo):
	headline = models.CharField(u'Headline', max_length=100)
	body = models.TextField(u'Content')
	
	class Meta:
		verbose_name=u'Article'
		verbose_name_plural=u'Articles'
		ordering = ['-date_updated']
		
	def __unicode__(self):
		return self.headline

	@models.permalink
	def get_absolute_url(self):
		return ('news_article_detail', (), {'pk': self.pk})
