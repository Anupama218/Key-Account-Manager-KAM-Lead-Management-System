# leads/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Lead
from .serializers import LeadSerializer
from interaction.models import Interaction

class LeadListCreateView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LeadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CalculateAccountPerformanceView(generics.GenericAPIView):
    """
    View to calculate and return account performance metrics for a specific lead.
    """
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    def get(self, request, lead_id):
        try:
            lead = Lead.objects.get(lead_id=lead_id)
            # Retrieve all interactions related to the lead
            interactions = Interaction.objects.filter(lead_id=lead_id)
            
            total_interactions = interactions.count()
            successful_interactions = interactions.filter(call_status='successful').count()  # Count successful interactions
            
            # Calculate performance metrics
            success_rate = (successful_interactions / total_interactions) * 100 if total_interactions > 0 else 0
            performance_data = {
                'total_interactions': total_interactions,
                'successful_interactions': successful_interactions,
                'success_rate': success_rate,
                'lead_status': lead.status,
            }
            
            return Response(performance_data, status=status.HTTP_200_OK)
        
        except Lead.DoesNotExist:
            return Response({"error": "Lead not found."}, status=status.HTTP_404_NOT_FOUND)