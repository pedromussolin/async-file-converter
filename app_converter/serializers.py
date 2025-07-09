from rest_framework import serializers
from .models import FileType, Conversion

class FileTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileType
        fields = ['id', 'name', 'extension', 'description', 'is_active']

class ConversionSerializer(serializers.ModelSerializer):
    input_type = FileTypeSerializer(read_only=True)
    output_type = FileTypeSerializer(read_only=True)

    class Meta:
        model = Conversion
        fields = ['id', 'input_file', 'output_file', 'input_type', 'output_type', 'status', 'created_at', 'updated_at', 'log']
        read_only_fields = ['output_file', 'status', 'created_at', 'updated_at', 'log']
