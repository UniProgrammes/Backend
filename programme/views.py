from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from .models import Programme
from .serializers import ProgrammeSerializer

class ProgrammeViewSet(GenericViewSet, ListModelMixin):
    queryset = Programme.objects.all()
    serializer_class = ProgrammeSerializer

    def list(self, request):
        programme_id = request.query_params.get('id', None)
        if programme_id:
            try:
                programme = self.queryset.get(programmeid=programme_id)
                serializer = self.serializer_class(programme)
                return Response(serializer.data)
            except Programme.DoesNotExist:
                return Response({'error': 'Programme not found'}, status=404)
        
        programmes = self.queryset.all()
        serializer = self.serializer_class(programmes, many=True)
        return Response(serializer.data)