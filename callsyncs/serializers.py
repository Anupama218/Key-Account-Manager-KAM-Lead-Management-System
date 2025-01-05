# Contacts/serializers.py

from rest_framework import serializers
from .models import CallSync

class CallSyncSerializer(serializers.ModelSerializer):
    scheduled_date = serializers.DateTimeField(input_formats=["%Y-%m-%dT%H:%M:%S"])
    last_called = serializers.DateTimeField(input_formats=["%Y-%m-%dT%H:%M:%S"])
    class Meta:
        model = CallSync
        fields = ['call_id', 'lead_id', 'scheduled_date','timezone', 'last_called']
