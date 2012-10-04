# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Style'
        db.create_table('onlineresume_style', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('onlineresume', ['Style'])

        # Adding model 'Person'
        db.create_table('onlineresume_person', (
            ('person_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['curriculumvitae.Person'], unique=True, primary_key=True)),
            ('curriculum_vitae_style', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['onlineresume.Style'])),
        ))
        db.send_create_signal('onlineresume', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Style'
        db.delete_table('onlineresume_style')

        # Deleting model 'Person'
        db.delete_table('onlineresume_person')


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
            'person_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['curriculumvitae.Person']", 'unique': 'True', 'primary_key': 'True'})
        },
        'onlineresume.style': {
            'Meta': {'object_name': 'Style'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['onlineresume']