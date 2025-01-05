# CallSyncs/urls.py

from django.urls import path
from .views import CallSyncListCreateView, CallSyncDetailView, TodaysCallsView
from rest_framework import routers

# router = routers.DefaultRouter

# router.register(r'create', CallSyncListCreateView)
# router.register(r'update', CallSyncDetailView)
urlpatterns = [
    path('callsyncs/', CallSyncListCreateView.as_view(), name='CallSync-list-create'),
    path('callsyncs/<int:pk>/', CallSyncDetailView.as_view(), name='CallSync-detail'),
    path('callsyncs/today/', TodaysCallsView.as_view(), name='todays_calls'),
]
