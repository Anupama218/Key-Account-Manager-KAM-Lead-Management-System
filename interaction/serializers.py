# Contacts/serializers.py

from rest_framework import serializers
from .models import Interaction

class InteractionSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(input_formats=["%Y-%m-%dT%H:%M:%S"])
    class Meta:
        model = Interaction
        fields = ['interaction_id', 'lead_id', 'date','timezone', 'type', 'call_status']
