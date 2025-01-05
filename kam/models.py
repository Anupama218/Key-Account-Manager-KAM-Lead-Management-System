# KAMs/models.py

from django.db import models

class KAM(models.Model):
   
    kam_id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=15, unique=True)
    account_id = models.IntegerField()
    
    def __str__(self):
        return self.kam_id

    class Meta:
        verbose_name = "KAM"
        verbose_name_plural = "KAMs"
