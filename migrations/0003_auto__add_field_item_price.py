# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.price'
        db.add_column('foods_item', 'price',
                      self.gf('django.db.models.fields.DecimalField')(blank=True, max_digits=5, null=True, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Item.price'
        db.delete_column('foods_item', 'price')


    models = {
        'foods.item': {
            'Meta': {'object_name': 'Item'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'market': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '5', 'null': 'True', 'decimal_places': '2'}),
            'purchased': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'purchased_date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['foods']