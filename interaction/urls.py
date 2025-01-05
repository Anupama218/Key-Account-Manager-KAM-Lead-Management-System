# Interactions/urls.py

from django.urls import path
from .views import InteractionListCreateView, InteractionDetailView
from rest_framework import routers

# router = routers.DefaultRouter

# router.register(r'create', InteractionListCreateView)
# router.register(r'update', InteractionDetailView)
urlpatterns = [
    path('interaction/', InteractionListCreateView.as_view(), name='interaction-list-create'),
    path('interaction/<int:pk>/', InteractionDetailView.as_view(), name='interaction-detail'),
    
]
