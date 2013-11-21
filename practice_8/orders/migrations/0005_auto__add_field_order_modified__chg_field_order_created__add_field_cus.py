# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Order.modified'
        db.add_column(u'orders_order', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(
                          auto_now=True, default=datetime.datetime(
                              2013, 11, 9, 0, 0), blank=True),
                      keep_default=False)

        # Changing field 'Order.created'
        db.alter_column(u'orders_order', 'created', self.gf(
            'django.db.models.fields.DateTimeField')(auto_now_add=True))
        # Adding field 'Customer.created'
        db.add_column(u'orders_customer', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(
                          auto_now_add=True, default=datetime.datetime(
                              2013, 11, 9, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Customer.modified'
        db.add_column(u'orders_customer', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(
                          auto_now=True, default=datetime.datetime(
                              2013, 11, 9, 0, 0), blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Order.modified'
        db.delete_column(u'orders_order', 'modified')

        # Changing field 'Order.created'
        db.alter_column(u'orders_order', 'created',
                        self.gf('django.db.models.fields.DateField')())
        # Deleting field 'Customer.created'
        db.delete_column(u'orders_customer', 'created')

        # Deleting field 'Customer.modified'
        db.delete_column(u'orders_customer', 'modified')

    models = {
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
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 9, 0, 0)'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
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
        },
        u'orders.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'orders.order': {
            'Meta': {'object_name': 'Order'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orders.Customer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemld': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Book']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['orders']
