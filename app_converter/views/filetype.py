from rest_framework import viewsets
from app_converter.models import FileType
from app_converter.serializers import FileTypeSerializer

class FileTypeViewSet(viewsets.ModelViewSet):
    queryset = FileType.objects.all()
    serializer_class = FileTypeSerializer
