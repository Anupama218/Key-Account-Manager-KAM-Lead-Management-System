# Interactions/models.py

from django.db import models

class Interaction(models.Model):
    interaction_id = models.CharField(max_length=55, primary_key=True)
    lead_id = models.CharField(max_length=50)
    date = models.DateTimeField()   
    timezone = models.CharField(max_length=20) 
    type = models.CharField(max_length=255)
    call_status = models.TextField()

    def __str__(self):
        return self.interaction_id

    class Meta:
        verbose_name = "Interaction"
        verbose_name_plural = "Interactions"
