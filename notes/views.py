from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    
    def create(self, request, *args, **kwargs):
        """Create a new note"""
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def hello_world(request):
    """Test endpoint to check connection"""
    return Response({
        'message': 'Hello from Django! Connection successful.',
        'status': 'Connected',
        'total_notes': Note.objects.count()
    })