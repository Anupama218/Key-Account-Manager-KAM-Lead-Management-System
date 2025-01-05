# leads/urls.py

from django.urls import path
from .views import LeadListCreateView, LeadDetailView
from rest_framework import routers

# router = routers.DefaultRouter

# router.register(r'create', LeadListCreateView)
# router.register(r'update', LeadDetailView)
urlpatterns = [
    path('leads/', LeadListCreateView.as_view(), name='lead-list-create'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    
]
