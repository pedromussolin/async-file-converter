from celery import shared_task
from app_converter.models import Conversion

def fake_conversion(input_path, output_path):
    # Simula uma conversão de arquivo (apenas copia o arquivo)
    import shutil
    shutil.copy(input_path, output_path)

@shared_task
def convert_file_task(conversion_id):
    from django.core.files import File
    from django.conf import settings
    import os
    try:
        conversion = Conversion.objects.get(id=conversion_id)
        conversion.status = 'processing'
        conversion.save()
        input_path = conversion.input_file.path
        output_ext = conversion.output_type.extension
        output_name = os.path.splitext(os.path.basename(input_path))[0] + output_ext
        output_path = os.path.join(settings.MEDIA_ROOT, 'converted', output_name)
        fake_conversion(input_path, output_path)
        with open(output_path, 'rb') as f:
            conversion.output_file.save(output_name, File(f), save=True)
        conversion.status = 'done'
        conversion.log = 'Conversão concluída com sucesso.'
        conversion.save()
    except Exception as e:
        conversion.status = 'failed'
        conversion.log = str(e)
        conversion.save()
