# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.purchased'
        db.add_column('foods_item', 'purchased',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Item.purchased_date'
        db.add_column('foods_item', 'purchased_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Item.market'
        db.add_column('foods_item', 'market',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=20, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Item.purchased'
        db.delete_column('foods_item', 'purchased')

        # Deleting field 'Item.purchased_date'
        db.delete_column('foods_item', 'purchased_date')

        # Deleting field 'Item.market'
        db.delete_column('foods_item', 'market')


    models = {
        'foods.item': {
            'Meta': {'object_name': 'Item'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '20', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'purchased': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'purchased_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['foods']