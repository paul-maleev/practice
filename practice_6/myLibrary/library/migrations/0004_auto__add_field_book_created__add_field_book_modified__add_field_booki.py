# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Book.created'
        db.add_column(u'library_book', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(
                          auto_now_add=True, default=datetime.datetime(
                              2013, 11, 2, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Book.modified'
        db.add_column(u'library_book', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(
                          auto_now=True, default=datetime.datetime(
                              2013, 11, 2, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'BookImage.created'
        db.add_column(u'library_bookimage', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(
                          auto_now_add=True, default=datetime.datetime(
                              2013, 11, 2, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'BookImage.modified'
        db.add_column(u'library_bookimage', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(
                          auto_now=True, default=datetime.datetime(
                              2013, 11, 2, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Publisher.created'
        db.add_column(u'library_publisher', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(
                          auto_now_add=True, default=datetime.datetime(
                              2013, 11, 2, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Publisher.modified'
        db.add_column(u'library_publisher', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(
                          auto_now=True, default=datetime.datetime(
                              2013, 11, 2, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Author.created'
        db.add_column(u'library_author', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(
                          auto_now_add=True, default=datetime.datetime(
                              2013, 11, 2, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Author.modified'
        db.add_column(u'library_author', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(
                          auto_now=True, default=datetime.datetime(
                              2013, 11, 2, 0, 0), blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Book.created'
        db.delete_column(u'library_book', 'created')

        # Deleting field 'Book.modified'
        db.delete_column(u'library_book', 'modified')

        # Deleting field 'BookImage.created'
        db.delete_column(u'library_bookimage', 'created')

        # Deleting field 'BookImage.modified'
        db.delete_column(u'library_bookimage', 'modified')

        # Deleting field 'Publisher.created'
        db.delete_column(u'library_publisher', 'created')

        # Deleting field 'Publisher.modified'
        db.delete_column(u'library_publisher', 'modified')

        # Deleting field 'Author.created'
        db.delete_column(u'library_author', 'created')

        # Deleting field 'Author.modified'
        db.delete_column(u'library_author', 'modified')

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'library.author': {
            'Meta': {'object_name': 'Author'},
            'birth_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'library.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Author']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 2, 0, 0)'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'library.bookimage': {
            'Meta': {'object_name': 'BookImage'},
            'book_cover': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Book']"}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'large_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'small_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'library.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['library']
