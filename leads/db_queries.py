from .models import Lead

def get_all_Leadss():
    return Lead.objects.all()

def get_Leads_by_id(lead_id):
    try:
        return Lead.objects.get(lead_id=lead_id)
    except Lead.DoesNotExist:
        return None

def create_Leads(data):
    Leads = Leads(**data)
    Leads.save()
    return Leads

# Add more query functions as needed...
