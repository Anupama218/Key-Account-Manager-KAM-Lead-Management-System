# ccount/urls.py

from django.urls import path
from .views import AccountListCreateView, AccountDetailView

urlpatterns = [
    path('account/', AccountListCreateView.as_view(), name='Account-list-create'),
    path('account/<int:pk>/', AccountDetailView.as_view(), name='Account-detail'),
    
]
