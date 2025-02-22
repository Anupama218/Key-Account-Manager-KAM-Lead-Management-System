# Contacts/serializers.py

from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['contact_id', 'name', 'contact_number', 'lead_id', 'role']
