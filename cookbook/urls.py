from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^user/', include('userauth.urls')),
    
    url(r'^news/', include('news.urls')),
    
    url(r'^', include('recipes.urls')),
 
	
)
