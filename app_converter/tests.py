from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import FileType, Conversion
from django.core.files.uploadedfile import SimpleUploadedFile

class FileTypeAPITests(APITestCase):
    def setUp(self):
        self.filetype = FileType.objects.create(name='PDF', extension='.pdf', is_active=True)

    def test_list_filetypes(self):
        url = reverse('filetype-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_filetype(self):
        url = reverse('filetype-list')
        data = {'name': 'DOCX', 'extension': '.docx', 'is_active': True}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_filetype_invalid(self):
        url = reverse('filetype-list')
        data = {'name': '', 'extension': '', 'is_active': True}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_filetype(self):
        url = reverse('filetype-detail', args=[self.filetype.id])
        data = {'name': 'PDF Atualizado', 'extension': '.pdf', 'is_active': False}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'PDF Atualizado')
        self.assertFalse(response.data['is_active'])

    def test_delete_filetype(self):
        url = reverse('filetype-detail', args=[self.filetype.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ConversionAPITests(APITestCase):
    def setUp(self):
        self.input_type = FileType.objects.create(name='PDF', extension='.pdf', is_active=True)
        self.output_type = FileType.objects.create(name='DOCX', extension='.docx', is_active=True)

    def test_create_conversion(self):
        url = reverse('file-convert')
        file_content = b'%PDF-1.4 test content'
        test_file = SimpleUploadedFile('test.pdf', file_content, content_type='application/pdf')
        data = {
            'file': test_file,
            'formato_destino': 'docx',
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['input_type']['extension'], '.pdf')
        self.assertEqual(response.data['output_type']['extension'], '.docx')

    def test_list_conversions(self):
        Conversion.objects.create(
            input_file=SimpleUploadedFile('test.pdf', b'data'),
            input_type=self.input_type,
            output_type=self.output_type,
            status='pending',
        )
        url = reverse('conversion-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_conversion_invalid_format(self):
        url = reverse('file-convert')
        file_content = b'%PDF-1.4 test content'
        test_file = SimpleUploadedFile('test.pdf', file_content, content_type='application/pdf')
        data = {
            'file': test_file,
            'formato_destino': 'xlsx',  # formato não cadastrado
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_conversion_missing_file(self):
        url = reverse('file-convert')
        data = {'formato_destino': 'docx'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_conversion_missing_format(self):
        url = reverse('file-convert')
        file_content = b'%PDF-1.4 test content'
        test_file = SimpleUploadedFile('test.pdf', file_content, content_type='application/pdf')
        data = {'file': test_file}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
