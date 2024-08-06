# Extrair URLs de PDFs

Este projeto contém um script Python que extrai todas as URLs de um arquivo PDF, incluindo URLs encontradas em texto e em imagens dentro do PDF.

## Requisitos

- Python 3
- Bibliotecas Python: `pymupdf`, `pytesseract`, `pdf2image`
- Poppler (para manipulação de PDFs)
- Tesseract-OCR => https://github.com/tesseract-ocr/tesseract

## Instalação

### No Debian/Ubuntu

```bash
sudo apt install python3-venv python3-pip
sudo apt install tesseract-ocr poppler-utils
````

## Uso

Configurar o Caminho do PDF e do Arquivo de Saída

No script, altere as variáveis pdf_path e output_txt_path para o caminho do seu arquivo PDF e o caminho onde você quer salvar o arquivo de texto com as URLs extraídas. Por exemplo:

python

pdf_path = 'caminho/para/seu_arquivo.pdf'
output_txt_path = 'caminho/para/urls_extraidas.txt'

Coloque o caminho do arquivo PDF no script extrair_urls.py e execute:
![image](https://github.com/user-attachments/assets/31abdab4-dc78-4af1-aab8-75faea15d953)


```bash
python extrair_urls.py
````

Este script faz o seguinte:

- Abre o arquivo PDF utilizando PyMuPDF.
- Extrai textos e links de cada página do PDF.
- Utiliza pdf2image para converter páginas PDF em imagens e pytesseract para realizar OCR (Reconhecimento Óptico de Caracteres) nas imagens.
- Utiliza uma expressão regular para encontrar URLs no texto e nas imagens.
- Remove URLs duplicadas e as escreve em um arquivo de texto.

Certifique-se de ajustar os caminhos do arquivo PDF e do arquivo de saída conforme necessário.

Resultado

Depois de executar o script, você deverá ter um arquivo de texto (urls_extraidas.txt) contendo todas as URLs extraídas do seu arquivo PDF, tanto das partes de texto quanto das imagens.
Dicas

Verifique o Tesseract OCR: Se você encontrar problemas ao converter imagens para texto, verifique se o Tesseract OCR está corretamente instalado e configurado no seu PATH do sistema.
Revisão do PDF: PDFs com muitas imagens ou elementos gráficos complexos podem ter URLs que o OCR não reconheça perfeitamente. Verifique o arquivo de saída e, se necessário, ajuste manualmente.


