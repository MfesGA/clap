# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Loca_main.Loca_lat'
        db.alter_column(u'restaurants_loca_main', 'Loca_lat', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=7))

        # Changing field 'Loca_main.Loca_long'
        db.alter_column(u'restaurants_loca_main', 'Loca_long', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=7))

    def backwards(self, orm):

        # Changing field 'Loca_main.Loca_lat'
        db.alter_column(u'restaurants_loca_main', 'Loca_lat', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Loca_main.Loca_long'
        db.alter_column(u'restaurants_loca_main', 'Loca_long', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'restaurants.loca_main': {
            'Loca_desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'Loca_lat': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '7'}),
            'Loca_long': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '7'}),
            'Meta': {'object_name': 'Loca_main'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'restaurants.minor_nts': {
            'Meta': {'object_name': 'Minor_nts'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nts_acc': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'nts_ano': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nts_path': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'nts_stdid': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'nts_uc': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['restaurants.Nts_course']"})
        },
        u'restaurants.minor_restaurant': {
            'Meta': {'object_name': 'Minor_restaurant'},
            'Rstr_chefs': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'Rstr_desc': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'Rstr_dlike': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Rstr_img': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'Rstr_like': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Rstr_loc': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['restaurants.Loca_main']"}),
            'Rstr_lot': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Rstr_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Rstr_rsoc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'Rstr_tcoz': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'Rstr_wsug': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'restaurants.nts_course': {
            'Meta': {'object_name': 'Nts_course'},
            'course_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'course_uc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'restaurants.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'Rstr_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurants.Minor_restaurant']"}),
            'Rstr_mail': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'Rstr_pass': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'restaurants.rstr_menu': {
            'Menu_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'Menu_desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'Menu_preco': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'Menu_rstr': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['restaurants.Restaurant']"}),
            'Meta': {'object_name': 'Rstr_menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['restaurants']