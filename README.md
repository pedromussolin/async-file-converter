# async-file-converter

Asynchronous file converter developed in Python using Django REST Framework, Celery, and Redis. It allows the conversion of various file types through a backend API, ideal for integration with graphical interfaces or other systems.

## Features
- Asynchronous file conversion with queue management (Celery + Redis)
- Support for multiple document, image, audio, video, and compressed file formats
- RESTful API for integration with frontends or automations
- Celery task monitoring via Flower
- Administration of file types and conversions via Django Admin

## Supported Formats
### Documents
- .pdf, .docx, .doc, .xlsx, .xls, .pptx, .ppt, .txt, .rtf, .odt, .ods, .odp, .epub, .mobi

### Images
- .jpeg, .jpg, .png, .gif, .bmp, .tiff, .tif, .svg, .ai, .eps

### Audio
- .mp3, .aac, .ogg, .wma, .flac, .alac, .wav, .aiff

### Video
- .mp4, .avi, .mov, .mkv, .wmv, .flv, .webm

### Compressed Files
- .zip, .rar, .7z, .tar.gz, .tgz

### Others
- .dwg, .dxf, .html, .htm, .xml, .json, .ttf, .otf

## Requirements
- Python 3.8+
- Virtualenv (recommended for isolated environment)
- Redis (broker for Celery)

## Installation and Running (Development)
1. Clone the repository:
   ```powershell
   git clone <repository-url>
   cd async-file-converter
   ```
2. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   pip install flower  # To monitor Celery
   ```
4. Run Django migrations:
   ```powershell
   python manage.py migrate
   ```
5. Start Redis (leave it running in a separate terminal):
   ```powershell
   redis-server
   ```
6. Start the Celery worker (in another terminal):
   ```powershell
   celery -A project_async_file_converter worker --loglevel=info --pool=solo
   ```
7. (Optional) Start Flower to monitor Celery tasks:
   ```powershell
   celery -A project_async_file_converter flower
   # Access http://localhost:5555
   ```
8. Start the Django development server:
   ```powershell
   python manage.py runserver
   ```

## API Usage
The API will be available at `http://127.0.0.1:8000/`.

### File upload for conversion
Send a POST to `/api/convert/` with a file and the `formato_destino` field:

**Example with curl:**
```powershell
curl -X POST http://127.0.0.1:8000/api/convert/ ^
  -F "file=@path/to/your/file.pdf" ^
  -F "formato_destino=png"
```

- The `formato_destino` field must be the extension of the registered output format (e.g., `docx`, `pdf`, `png`, etc., without the dot).
- To see all available formats, access `/api/file-types/`.

### Check conversion status
```http
GET /api/conversions/
```

### Administration
- Django Admin: http://127.0.0.1:8000/admin/
- Flower (Celery monitor): http://localhost:5555

## Automated Tests

The project includes a suite of automated tests to ensure the quality and correct functioning of the endpoints and asynchronous processing.

### How to run the tests

1. Make sure the virtual environment is activated and dependencies are installed.
2. Run the tests with the command:
   ```powershell
   python manage.py test
   ```
   Or to run only the app tests:
   ```powershell
   python manage.py test app_converter
   ```

### What is tested
- CRUD for allowed file types (`FileType`)
- File upload and conversion registration
- Listing of conversions
- Asynchronous conversion flow with Celery (integration tests)
- Validation of required fields and invalid formats

The tests ensure that the backend is working correctly, including integration with Celery and Redis.

## License
This project is licensed under the MIT license. See the [LICENSE](LICENSE) file for more details.

