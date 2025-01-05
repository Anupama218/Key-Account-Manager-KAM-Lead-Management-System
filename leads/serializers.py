# leads/serializers.py

from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['lead_id', 'restaurant_name', 'contact_number', 'email', 'address', 'status', 'created_at', 'updated_at']
