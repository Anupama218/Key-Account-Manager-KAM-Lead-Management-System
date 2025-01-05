# CallSyncs/models.py

from django.db import models

class CallSync(models.Model):
    call_id = models.CharField(max_length=55, primary_key=True)
    lead_id = models.CharField(max_length=50)
    scheduled_date = models.DateTimeField() 
    timezone = models.CharField(max_length=20)    
    last_called = models.DateTimeField()
    
    def __str__(self):
        return self.call_id

    class Meta:
        verbose_name = "CallSync"
        verbose_name_plural = "CallSyncs"
