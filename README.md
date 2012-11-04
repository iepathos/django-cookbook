### README.md for Cookbook - Django 1.4.2
## Based on a German cookbook webapp tutorial found here: [http://django-workshop.de](http://django-workshop.de)

### I created this site to demonstrate what I can do.  I list features here as I add them to the site.

Added custom templatetag

Created PDF view for recipes

Installed Tastypie for RESTful web service

Created RSS feed for news app

Extended Recipe model with custom manager ActiveRecipeManager

Created news app

Setup South to handle database migrations

Created router.py to manage multiple databases for the site

Created second database for news app

Improved templates to show author, difficulty and categories.

Created Middleware to handle 403 errors

Replaced index and detail functions with class-based-generic-views

Added frontend forms for adding and editing recipes to cookbook for users.

Updated render_to_response to render shortcut - DRY.

Created userauth to extend django.contrib.auth and provide user management.

Added staticfiles and HTML5 Boiler.

De-coupled URLconf and templates for best practice - DRY.

Database import with 3 German recipes: import.json

Database backup with banana pancakes and hummus recipes: backup.json

Setup local_settings.py to hold local development environment settings for best practice.

Initial functionality - Add recipes to your cookbook through admin interface
