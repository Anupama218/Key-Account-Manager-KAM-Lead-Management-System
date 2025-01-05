from .models import CallSync

def get_all_CallSyncs():
    return CallSync.objects.all()

def get_CallSync_by_id(call_id):
    try:
        return CallSync.objects.get(call_id=call_id)
    except CallSync.DoesNotExist:
        return None

def create_CallSync(data):
    CallSync = CallSync(**data)
    CallSync.save()
    return CallSync

# Add more query functions as needed...
