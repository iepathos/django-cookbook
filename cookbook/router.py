class CookbookRouter(object):
	""" A router for database management in cookbook site """
	
	def db_for_read(self, model, **hints):
		if model._meta.app_label == 'news':
			return 'newsdb'
		return None
		
	def db_for_write(self, model, **hints):
		if model._meta.app_label == 'news':
			return 'newsdb'
		return None
		
	def allow_relation(self, obj1, obj2, **hints):
		if obj1._meta.app_label == 'news' or obj2._meta.app_label == 'news':
			return False
		return None

	def allow_syncdb(self, db, model):
		allowed = ['south']
		if model._meta.app_label in allowed:
			return True
		elif db == 'newsdb':
			return model._meta.app_label == 'news'
		elif model._meta.app_label == 'news':
			return False
		return None
