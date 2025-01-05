# services/business_logic.py

from datetime import datetime
from leads.models import Lead  
from callsyncs.models import CallSync  
from interaction.models import Interaction

def get_todays_calls():
    today = datetime.now().date()
    return CallSync.objects.filter(scheduled_date=today)

def calculate_account_performance(id):
    try:
        lead = Lead.objects.get(lead_id=id)
        # Retrieve all interactions related to the lead
        interactions = Interaction.objects.filter(lead_id=id)
        
        total_interactions = interactions.count()
        successful_interactions = interactions.filter(call_status='successful').count()  # Count successful interactions
        
        # Calculate performance metrics
        success_rate = (successful_interactions / total_interactions) * 100 if total_interactions > 0 else 0
        
        return {
            'total_interactions': total_interactions,
            'successful_interactions': successful_interactions,
            'success_rate': success_rate,
            'lead_status': lead.status,
        }
    except Lead.DoesNotExist:
        None

def update_lead_status(lead_id, new_status):
    try:
        lead = Lead.objects.get(lead_id=lead_id)
        lead.status = new_status
        lead.save()
        return True
    except Lead.DoesNotExist:
        return False
