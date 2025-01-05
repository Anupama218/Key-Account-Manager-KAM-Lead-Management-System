from .models import Contact

def get_all_Contacts():
    return Contact.objects.all()

def get_Contact_by_id(contact_id):
    try:
        return Contact.objects.get(Contact_id=Contact_id)
    except Contact.DoesNotExist:
        return None

def create_Contact(data):
    Contact = Contact(**data)
    Contact.save()
    return Contact

# Add more query functions as needed...
