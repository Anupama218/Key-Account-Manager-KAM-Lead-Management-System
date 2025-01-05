from .models import Interaction

def get_all_Interactions():
    return Interaction.objects.all()

def get_Interaction_by_id(Interaction_id):
    try:
        return Interaction.objects.get(interaction_id=Interaction_id)
    except Interaction.DoesNotExist:
        return None

def create_Interaction(data):
    Interaction = Interaction(**data)
    Interaction.save()
    return Interaction

# Add more query functions as needed...
