# leads/urls.py

from django.urls import path
from .views import LeadListCreateView, LeadDetailView, CalculateAccountPerformanceView

urlpatterns = [
    path('leads/', LeadListCreateView.as_view(), name='lead-list-create'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('leads/performance/<int:lead_id>/', CalculateAccountPerformanceView.as_view(), name='calculate_account_performance')
]
