# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Minor_restaurant'
        db.create_table(u'restaurants_minor_restaurant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Rstr_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('Rstr_like', self.gf('django.db.models.fields.IntegerField')()),
            ('Rstr_dlike', self.gf('django.db.models.fields.IntegerField')()),
            ('Rstr_wsug', self.gf('django.db.models.fields.BooleanField')()),
            ('Rstr_desc', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal(u'restaurants', ['Minor_restaurant'])

        # Adding model 'Restaurant'
        db.create_table(u'restaurants_restaurant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Rstr_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurants.Minor_restaurant'])),
            ('Rstr_pass', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('Rstr_mail', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'restaurants', ['Restaurant'])

        # Adding model 'Rstr_menu'
        db.create_table(u'restaurants_rstr_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Menu_date', self.gf('django.db.models.fields.DateField')()),
            ('Menu_desc', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('Menu_rstr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurants.Restaurant'])),
        ))
        db.send_create_signal(u'restaurants', ['Rstr_menu'])

        # Adding model 'Minor_loca'
        db.create_table(u'restaurants_minor_loca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Loca_desc', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('Loca_lat', self.gf('django.db.models.fields.IntegerField')()),
            ('Loca_long', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'restaurants', ['Minor_loca'])

        # Adding model 'Nts_course'
        db.create_table(u'restaurants_nts_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course_uc', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('course_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'restaurants', ['Nts_course'])

        # Adding model 'Minor_nts'
        db.create_table(u'restaurants_minor_nts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nts_path', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('nts_acc', self.gf('django.db.models.fields.BooleanField')()),
            ('nts_stdid', self.gf('django.db.models.fields.IntegerField')()),
            ('nts_ano', self.gf('django.db.models.fields.IntegerField')()),
            ('nts_uc', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurants.Nts_course'])),
        ))
        db.send_create_signal(u'restaurants', ['Minor_nts'])


    def backwards(self, orm):
        # Deleting model 'Minor_restaurant'
        db.delete_table(u'restaurants_minor_restaurant')

        # Deleting model 'Restaurant'
        db.delete_table(u'restaurants_restaurant')

        # Deleting model 'Rstr_menu'
        db.delete_table(u'restaurants_rstr_menu')

        # Deleting model 'Minor_loca'
        db.delete_table(u'restaurants_minor_loca')

        # Deleting model 'Nts_course'
        db.delete_table(u'restaurants_nts_course')

        # Deleting model 'Minor_nts'
        db.delete_table(u'restaurants_minor_nts')


    models = {
        u'restaurants.minor_loca': {
            'Loca_desc': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'Loca_lat': ('django.db.models.fields.IntegerField', [], {}),
            'Loca_long': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'Minor_loca'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'restaurants.minor_nts': {
            'Meta': {'object_name': 'Minor_nts'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nts_acc': ('django.db.models.fields.BooleanField', [], {}),
            'nts_ano': ('django.db.models.fields.IntegerField', [], {}),
            'nts_path': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nts_stdid': ('django.db.models.fields.IntegerField', [], {}),
            'nts_uc': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurants.Nts_course']"})
        },
        u'restaurants.minor_restaurant': {
            'Meta': {'object_name': 'Minor_restaurant'},
            'Rstr_desc': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'Rstr_dlike': ('django.db.models.fields.IntegerField', [], {}),
            'Rstr_like': ('django.db.models.fields.IntegerField', [], {}),
            'Rstr_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Rstr_wsug': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'restaurants.nts_course': {
            'Meta': {'object_name': 'Nts_course'},
            'course_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'course_uc': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'restaurants.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'Rstr_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurants.Minor_restaurant']"}),
            'Rstr_mail': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'Rstr_pass': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'restaurants.rstr_menu': {
            'Menu_date': ('django.db.models.fields.DateField', [], {}),
            'Menu_desc': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'Menu_rstr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurants.Restaurant']"}),
            'Meta': {'object_name': 'Rstr_menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['restaurants']