# ccount/urls.py

from django.urls import path
from .views import KAMListCreateView, KAMDetailView

urlpatterns = [
    path('kam/', KAMListCreateView.as_view(), name='kam-list-create'),
    path('kam/<int:pk>/', KAMDetailView.as_view(), name='kam-detail'),
    
]
