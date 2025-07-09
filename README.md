# async-file-converter

Conversor de arquivos com fila assíncrona, desenvolvido em Python utilizando Django REST Framework, Celery e Redis. Permite a conversão de diversos tipos de arquivos por meio de uma API backend, ideal para integração com interfaces gráficas ou outros sistemas.

## Funcionalidades
- Conversão assíncrona de arquivos com gerenciamento de fila (Celery + Redis)
- Suporte a múltiplos formatos de documentos, imagens, áudio, vídeo e arquivos compactados
- API RESTful para integração com frontends ou automações
- Monitoramento de tarefas Celery via Flower
- Administração dos tipos de arquivos e conversões via Django Admin

## Formatos Suportados
### Documentos
- .pdf, .docx, .doc, .xlsx, .xls, .pptx, .ppt, .txt, .rtf, .odt, .ods, .odp, .epub, .mobi

### Imagens
- .jpeg, .jpg, .png, .gif, .bmp, .tiff, .tif, .svg, .ai, .eps

### Áudio
- .mp3, .aac, .ogg, .wma, .flac, .alac, .wav, .aiff

### Vídeo
- .mp4, .avi, .mov, .mkv, .wmv, .flv, .webm

### Arquivos e Compactados
- .zip, .rar, .7z, .tar.gz, .tgz

### Outros
- .dwg, .dxf, .html, .htm, .xml, .json, .ttf, .otf

## Requisitos
- Python 3.8+
- Virtualenv (recomendado para ambiente isolado)
- Redis (broker para Celery)

## Instalação e Execução (Desenvolvimento)
1. Clone o repositório:
   ```powershell
   git clone <url-do-repositorio>
   cd async-file-converter
   ```
2. Crie e ative um ambiente virtual:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```
3. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   pip install flower  # Para monitorar o Celery
   ```
4. Execute as migrações do Django:
   ```powershell
   python manage.py migrate
   ```
5. Inicie o Redis (deixe rodando em um terminal separado):
   ```powershell
   redis-server
   ```
6. Inicie o worker Celery (em outro terminal):
   ```powershell
   celery -A project_async_file_converter worker --loglevel=info --pool=solo
   ```
7. (Opcional) Inicie o Flower para monitorar as tasks Celery:
   ```powershell
   celery -A project_async_file_converter flower
   # Acesse http://localhost:5555
   ```
8. Inicie o servidor de desenvolvimento Django:
   ```powershell
   python manage.py runserver
   ```

## Utilização da API
A API estará disponível em `http://127.0.0.1:8000/`.

### Upload de arquivo para conversão
Faça um POST para `/api/convert/` com um arquivo e o campo `formato_destino`:

**Exemplo com curl:**
```powershell
curl -X POST http://127.0.0.1:8000/api/convert/ ^
  -F "file=@caminho/do/seu/arquivo.pdf" ^
  -F "formato_destino=png"
```

- O campo `formato_destino` deve ser a extensão do formato de saída cadastrado (ex: `docx`, `pdf`, `png`, etc, sem o ponto).
- Para ver todos os formatos disponíveis, acesse `/api/file-types/`.

### Consultar status das conversões
```http
GET /api/conversions/
```

### Administração
- Django Admin: http://127.0.0.1:8000/admin/
- Flower (monitor Celery): http://localhost:5555

## Licença
Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

