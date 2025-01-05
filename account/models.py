# Accounts/models.py

from django.db import models

class Account(models.Model):
   
    account_id = models.IntegerField( primary_key=True)
    lead_ids = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.account_id

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
