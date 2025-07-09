# async-file-converter

Conversor de arquivos com fila assíncrona, desenvolvido em Python utilizando Django REST Framework. Permite a conversão de diversos tipos de arquivos por meio de uma API backend, ideal para integração com interfaces gráficas ou outros sistemas.

## Funcionalidades
- Conversão assíncrona de arquivos com gerenciamento de fila
- Suporte a múltiplos formatos de documentos, imagens, áudio, vídeo e arquivos compactados
- API RESTful para integração com frontends ou automações

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
   ```
4. Execute as migrações do Django:
   ```powershell
   python manage.py migrate
   ```
5. Inicie o servidor de desenvolvimento:
   ```powershell
   python manage.py runserver
   ```

## Uso
A API estará disponível em `http://127.0.0.1:8000/`. Consulte a documentação dos endpoints (exemplo: `/docs/` se usar drf-yasg ou drf-spectacular).

### Exemplo de requisição (upload de arquivo para conversão)
```http
POST /api/convert/
Content-Type: multipart/form-data

file=@exemplo.pdf
formato_destino=docx
```

## Licença
Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Se precisar de exemplos de endpoints ou payloads específicos, ou quiser personalizar mais alguma seção, é só avisar!
