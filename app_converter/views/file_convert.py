from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from app_converter.models import FileType, Conversion
from app_converter.serializers import ConversionSerializer
from app_converter.tasks import convert_file_task

class FileConvertView(generics.CreateAPIView):
    serializer_class = ConversionSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        input_file = request.FILES.get('file')
        formato_destino = request.data.get('formato_destino')
        if not input_file or not formato_destino:
            return Response({'error': 'Arquivo e formato_destino são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)
        input_ext = input_file.name.split('.')[-1].lower()
        input_type = get_object_or_404(FileType, extension=f'.{input_ext}', is_active=True)
        output_type = get_object_or_404(FileType, extension=f'.{formato_destino}', is_active=True)
        conversion = Conversion.objects.create(
            input_file=input_file,
            input_type=input_type,
            output_type=output_type,
            status='pending',
        )
        convert_file_task.delay(conversion.id)
        return Response(ConversionSerializer(conversion).data, status=status.HTTP_201_CREATED)
