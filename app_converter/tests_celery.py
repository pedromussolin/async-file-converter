from django.test import TestCase
from app_converter.tasks import convert_file_task
from app_converter.models import FileType, Conversion
from django.core.files.uploadedfile import SimpleUploadedFile
import time

class CeleryIntegrationTest(TestCase):
    def setUp(self):
        self.input_type = FileType.objects.create(name='PDF', extension='.pdf', is_active=True)
        self.output_type = FileType.objects.create(name='DOCX', extension='.docx', is_active=True)

    def test_celery_conversion_task(self):
        test_file = SimpleUploadedFile('test.pdf', b'data', content_type='application/pdf')
        conversion = Conversion.objects.create(
            input_file=test_file,
            input_type=self.input_type,
            output_type=self.output_type,
            status='pending',
        )
        result = convert_file_task.delay(conversion.id)
        # Aguarda a task terminar (máx 10s)
        for _ in range(20):
            conversion.refresh_from_db()
            if conversion.status in ['done', 'failed']:
                break
            time.sleep(0.5)
        self.assertEqual(conversion.status, 'done')
        self.assertTrue(conversion.output_file)
