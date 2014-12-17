# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Minor_loca'
        db.delete_table(u'restaurants_minor_loca')

        # Adding model 'Loca_main'
        db.create_table(u'restaurants_loca_main', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Loca_desc', self.gf('django.db.models.fields.CharField')(default='', max_length=150)),
            ('Loca_lat', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('Loca_long', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'restaurants', ['Loca_main'])

        # Adding field 'Minor_restaurant.Rstr_img'
        db.add_column(u'restaurants_minor_restaurant', 'Rstr_img',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'Minor_restaurant.Rstr_chefs'
        db.add_column(u'restaurants_minor_restaurant', 'Rstr_chefs',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)

        # Adding field 'Minor_restaurant.Rstr_tcoz'
        db.add_column(u'restaurants_minor_restaurant', 'Rstr_tcoz',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30),
                      keep_default=False)

        # Adding field 'Minor_restaurant.Rstr_lot'
        db.add_column(u'restaurants_minor_restaurant', 'Rstr_lot',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Minor_restaurant.Rstr_loc'
        db.add_column(u'restaurants_minor_restaurant', 'Rstr_loc',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['restaurants.Loca_main']),
                      keep_default=False)

        # Adding field 'Minor_restaurant.Rstr_rsoc'
        db.add_column(u'restaurants_minor_restaurant', 'Rstr_rsoc',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=150),
                      keep_default=False)


        # Changing field 'Minor_restaurant.Rstr_desc'
        db.alter_column(u'restaurants_minor_restaurant', 'Rstr_desc', self.gf('django.db.models.fields.CharField')(max_length=300))
        # Adding field 'Rstr_menu.Menu_preco'
        db.add_column(u'restaurants_rstr_menu', 'Menu_preco',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Minor_loca'
        db.create_table(u'restaurants_minor_loca', (
            ('Loca_lat', self.gf('django.db.models.fields.IntegerField')()),
            ('Loca_desc', self.gf('django.db.models.fields.CharField')(max_length=150)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Loca_long', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'restaurants', ['Minor_loca'])

        # Deleting model 'Loca_main'
        db.delete_table(u'restaurants_loca_main')

        # Deleting field 'Minor_restaurant.Rstr_img'
        db.delete_column(u'restaurants_minor_restaurant', 'Rstr_img')

        # Deleting field 'Minor_restaurant.Rstr_chefs'
        db.delete_column(u'restaurants_minor_restaurant', 'Rstr_chefs')

        # Deleting field 'Minor_restaurant.Rstr_tcoz'
        db.delete_column(u'restaurants_minor_restaurant', 'Rstr_tcoz')

        # Deleting field 'Minor_restaurant.Rstr_lot'
        db.delete_column(u'restaurants_minor_restaurant', 'Rstr_lot')

        # Deleting field 'Minor_restaurant.Rstr_loc'
        db.delete_column(u'restaurants_minor_restaurant', 'Rstr_loc_id')

        # Deleting field 'Minor_restaurant.Rstr_rsoc'
        db.delete_column(u'restaurants_minor_restaurant', 'Rstr_rsoc')


        # Changing field 'Minor_restaurant.Rstr_desc'
        db.alter_column(u'restaurants_minor_restaurant', 'Rstr_desc', self.gf('django.db.models.fields.CharField')(max_length=150))
        # Deleting field 'Rstr_menu.Menu_preco'
        db.delete_column(u'restaurants_rstr_menu', 'Menu_preco')


    models = {
        u'restaurants.loca_main': {
            'Loca_desc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150'}),
            'Loca_lat': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Loca_long': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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