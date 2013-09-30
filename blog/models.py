from django.db import models
from django.contrib import admin
from tinymce import models as tinymce_models

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length=150)
	sub_title = models.CharField(max_length=150)
	#body = models.TextField()
	content = tinymce_models.HTMLField()
	#http://django-tinymce.googlecode.com/svn/tags/release-1.5/docs/.build/html/usage.html
	timestamp = models.DateTimeField(auto_now_add = True, blank = True)
	image = models.ImageField(upload_to = 'photos')
	alt_tag = models.CharField(max_length=150)
	slug = models.SlugField(max_length=40, unique=True)
	
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ('-timestamp',)

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ('title', 'timestamp')
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost, BlogPostAdmin)
