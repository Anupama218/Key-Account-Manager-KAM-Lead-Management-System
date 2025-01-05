from .models import KAM

def add_new_manager(data):
    KAM = KAM(**data)
    KAM.save()
    return KAM

# Add more query functions as needed...
