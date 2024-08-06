import os
import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
import re

def extract_urls_from_pdf(pdf_path, output_txt_path):
    if not os.path.exists(pdf_path):
        print(f"Arquivo não encontrado: {pdf_path}")
        return
    
    # Abrir o arquivo PDF
    pdf_document = fitz.open(pdf_path)
    
    # Expressão regular para encontrar URLs
    url_pattern = re.compile(r'(https?://\S+)')
    
    # Lista para armazenar URLs encontrados
    urls = []

    # Extraia URLs de textos e links no PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        
        # Extraia o texto da página
        text = page.get_text()
        
        # Encontre URLs no texto
        found_urls = url_pattern.findall(text)
        urls.extend(found_urls)
        
        # Extraia links da página
        links = page.get_links()
        for link in links:
            uri = link.get('uri')
            if uri:
                urls.append(uri)
    
    # Converta páginas PDF em imagens e use OCR para extrair URLs de imagens
    images = convert_from_path(pdf_path)
    for image in images:
        text_from_image = pytesseract.image_to_string(image)
        found_urls_in_image = url_pattern.findall(text_from_image)
        urls.extend(found_urls_in_image)
    
    # Remova duplicatas convertendo para um conjunto e de volta para uma lista
    urls = list(set(urls))
    
    # Escreva os URLs no arquivo de texto de saída
    with open(output_txt_path, 'w') as output_file:
        for url in urls:
            output_file.write(url + '\n')

# Example usage
pdf_path = '/caminho/para/seu_arquivo.pdf'  # Substitua pelo caminho correto do seu arquivo PDF
output_txt_path = 'urls_extraidas.txt'
extract_urls_from_pdf(pdf_path, output_txt_path)
