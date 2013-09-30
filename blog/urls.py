from django.conf.urls.defaults import *
from django.conf import settings
#from blog.views import archive

urlpatterns = patterns('',
	url(r'^$', 'blog.views.archive'),
)