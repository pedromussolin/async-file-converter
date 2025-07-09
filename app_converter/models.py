from django.db import models

# Create your models here.

class FileType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    extension = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.extension})"

class Conversion(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('processing', 'Processando'),
        ('done', 'Concluído'),
        ('failed', 'Falhou'),
    ]
    input_file = models.FileField(upload_to='uploads/')
    output_file = models.FileField(upload_to='converted/', blank=True, null=True)
    input_type = models.ForeignKey(FileType, related_name='input_type', on_delete=models.CASCADE)
    output_type = models.ForeignKey(FileType, related_name='output_type', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    log = models.TextField(blank=True)

    def __str__(self):
        return f"{self.input_file.name} -> {self.output_type.extension} ({self.status})"
