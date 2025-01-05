from .models import KAM
from django.core.exceptions import ObjectDoesNotExist

def add_new_manager(data):
    KAM = KAM(**data)
    KAM.save()
    return KAM

def replace_manager(id, data):
    try:
        # Retrieve the KAM instance by kam_id
        kam_instance = KAM.objects.get(kam_id=id)
        
        # Update fields if new values are provided
        if data.name is not None:
            kam_instance.name = data.name
        if data.status is not None:
            kam_instance.status = data.status
        if data.account_id is not None:
            kam_instance.account_id = data.account_id
        
        # Save the updated instance back to the database
        kam_instance.save()
        
        return {"message": "KAM updated successfully.", "kam": kam_instance}
    
    except ObjectDoesNotExist:
        return {"error": "KAM with the specified ID does not exist."}

# Add more query functions as needed...
