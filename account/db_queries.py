from .models import Account

def add_new_account(data):
    Account = Account(**data)
    Account.save()
    return Account

# Add more query functions as needed...
