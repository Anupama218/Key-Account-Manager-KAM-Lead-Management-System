# KAMs/serializers.py

from rest_framework import serializers
from .models import KAM

class KAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = KAM
        fields = ['kam_id', 'name', 'status', 'account_id']
