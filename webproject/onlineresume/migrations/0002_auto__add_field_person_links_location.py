# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Person.links_location'
        db.add_column('onlineresume_person', 'links_location',
                      self.gf('django.db.models.fields.CharField')(default='T', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Person.links_location'
        db.delete_column('onlineresume_person', 'links_location')


    models = {
        'curriculumvitae.person': {
            'Meta': {'object_name': 'Person'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mugshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'short_description_en': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_description_es': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'onlineresume.person': {
            'Meta': {'object_name': 'Person', '_ormbases': ['curriculumvitae.Person']},
            'curriculum_vitae_style': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['onlineresume.Style']"}),
            'links_location': ('django.db.models.fields.CharField', [], {'default': "'T'", 'max_length': '1'}),
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['curriculumvitae.Person']", 'unique': 'True', 'primary_key': 'True'})
        },
        'onlineresume.style': {
            'Meta': {'object_name': 'Style'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['onlineresume']