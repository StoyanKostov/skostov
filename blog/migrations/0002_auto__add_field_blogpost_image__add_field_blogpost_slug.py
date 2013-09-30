# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BlogPost.image'
        db.add_column(u'blog_blogpost', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default=datetime.datetime(2013, 8, 3, 0, 0), max_length=100),
                      keep_default=False)

        # Adding field 'BlogPost.slug'
        db.add_column(u'blog_blogpost', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=datetime.datetime(2013, 8, 3, 0, 0), unique=True, max_length=40),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BlogPost.image'
        db.delete_column(u'blog_blogpost', 'image')

        # Deleting field 'BlogPost.slug'
        db.delete_column(u'blog_blogpost', 'slug')


    models = {
        u'blog.blogpost': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'BlogPost'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['blog']