# Contacts/urls.py

from django.urls import path
from .views import ContactListCreateView, ContactDetailView
from rest_framework import routers

# router = routers.DefaultRouter

# router.register(r'create', ContactListCreateView)
# router.register(r'update', ContactDetailView)
urlpatterns = [
    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    
]
