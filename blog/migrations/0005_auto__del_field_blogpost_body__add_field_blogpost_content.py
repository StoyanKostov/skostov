# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BlogPost.body'
        db.delete_column(u'blog_blogpost', 'body')

        # Adding field 'BlogPost.content'
        db.add_column(u'blog_blogpost', 'content',
                      self.gf('tinymce.models.HTMLField')(default=datetime.datetime(2013, 8, 5, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'BlogPost.body'
        db.add_column(u'blog_blogpost', 'body',
                      self.gf('django.db.models.fields.TextField')(default=datetime.datetime(2013, 8, 5, 0, 0)),
                      keep_default=False)

        # Deleting field 'BlogPost.content'
        db.delete_column(u'blog_blogpost', 'content')


    models = {
        u'blog.blogpost': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'BlogPost'},
            'alt_tag': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'content': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '40'}),
            'sub_title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['blog']