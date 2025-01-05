from rest_framework import generics, status
from rest_framework.response import Response
from .models import CallSync
from .serializers import CallSyncSerializer

class CallSyncListCreateView(generics.ListCreateAPIView):
    """
    View to list all CallSync instances or create a new CallSync instance.
    """
    queryset = CallSync.objects.all()
    serializer_class = CallSyncSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CallSyncDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a CallSync instance.
    """
    queryset = CallSync.objects.all()
    serializer_class = CallSyncSerializer

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

