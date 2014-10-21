# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Drone'
        db.create_table(u'backend_api_drone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('is_online', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('next_event', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('backend_api', ['Drone'])

        # Adding model 'User'
        db.create_table(u'backend_api_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('backend_api', ['User'])

        # Adding M2M table for field drone_id on 'User'
        m2m_table_name = db.shorten_name(u'backend_api_user_drone_id')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            (u'user', models.ForeignKey(orm['backend_api.user'], null=False)),
            (u'drone', models.ForeignKey(orm['backend_api.drone'], null=False))
        ))
        db.create_unique(m2m_table_name, [u'user_id', u'drone_id'])

        # Adding model 'Event'
        db.create_table(u'backend_api_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('error_code', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('drone_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend_api.Drone'])),
        ))
        db.send_create_signal('backend_api', ['Event'])

        # Adding M2M table for field user_id on 'Event'
        m2m_table_name = db.shorten_name(u'backend_api_event_user_id')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            (u'event', models.ForeignKey(orm['backend_api.event'], null=False)),
            (u'user', models.ForeignKey(orm['backend_api.user'], null=False))
        ))
        db.create_unique(m2m_table_name, [u'event_id', u'user_id'])

        # Adding model 'Waypoint'
        db.create_table(u'backend_api_waypoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('take_photo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('event_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend_api.Event'])),
        ))
        db.send_create_signal('backend_api', ['Waypoint'])

        # Adding model 'Picture'
        db.create_table(u'backend_api_picture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['backend_api.Event'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('backend_api', ['Picture'])


    def backwards(self, orm):
        # Deleting model 'Drone'
        db.delete_table(u'backend_api_drone')

        # Deleting model 'User'
        db.delete_table(u'backend_api_user')

        # Removing M2M table for field drone_id on 'User'
        db.delete_table(db.shorten_name(u'backend_api_user_drone_id'))

        # Deleting model 'Event'
        db.delete_table(u'backend_api_event')

        # Removing M2M table for field user_id on 'Event'
        db.delete_table(db.shorten_name(u'backend_api_event_user_id'))

        # Deleting model 'Waypoint'
        db.delete_table(u'backend_api_waypoint')

        # Deleting model 'Picture'
        db.delete_table(u'backend_api_picture')


    models = {
        'backend_api.drone': {
            'Meta': {'object_name': 'Drone'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_online': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'next_event': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        'backend_api.event': {
            'Meta': {'object_name': 'Event'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'drone_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend_api.Drone']"}),
            'error_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user_id': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['backend_api.User']", 'symmetrical': 'False'})
        },
        'backend_api.picture': {
            'Meta': {'object_name': 'Picture'},
            'event_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend_api.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'backend_api.user': {
            'Meta': {'object_name': 'User'},
            'drone_id': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['backend_api.Drone']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'backend_api.waypoint': {
            'Meta': {'object_name': 'Waypoint'},
            'event_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['backend_api.Event']"}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'take_photo': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['backend_api']