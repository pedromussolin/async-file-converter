from rest_framework import viewsets
from app_converter.models import Conversion
from app_converter.serializers import ConversionSerializer

class ConversionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Conversion.objects.all()
    serializer_class = ConversionSerializer
