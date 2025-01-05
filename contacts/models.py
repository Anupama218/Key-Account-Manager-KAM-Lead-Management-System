# Contacts/models.py

from django.db import models

class Contact(models.Model):
    contact_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15, unique=True)
    lead_id = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
