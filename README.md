# Extrair URLs de PDFs

Este projeto contém um script Python que extrai todas as URLs de um arquivo PDF, incluindo URLs encontradas em texto e em imagens dentro do PDF.

## Requisitos

- Python 3
- Bibliotecas Python: `pymupdf`, `pytesseract`, `pdf2image`
- Poppler (para manipulação de PDFs)

## Instalação

### No Debian/Ubuntu

```bash
sudo apt install python3-venv python3-pip
sudo apt install tesseract-ocr poppler-utils

