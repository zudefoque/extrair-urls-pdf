import os
import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
import re


class Extractor:
    def __init__(self, pdf_path: str = None, output_txt_path: str = None):
        """
        Initialize the URLExtractor with paths for the input PDF and output text file.

        :param pdf_path: Path to the PDF file to extract URLs from.
        :param output_txt_path: Path to the output text file where URLs will be saved.
        """
        self.pdf_path = pdf_path
        self.output_txt_path = output_txt_path

    def extract_urls(self, save: bool = False) -> list:
        """
        Extracts URLs from the given PDF file and saves them to the specified text file.
        
        The method extracts URLs from:
        - Text content of each page in the PDF.
        - Hyperlinks in each page of the PDF.
        - Text extracted from images within the PDF.

        URLs found are written to the output text file, with one URL per line.
        """
        if not os.path.exists(self.pdf_path):
            print(f"File not found: {self.pdf_path}")
            return None
        
        pdf_document = fitz.open(self.pdf_path)
        
        url_pattern = re.compile(r'(https?://\S+)')
        
        urls = []

        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            
            text = page.get_text()
            
            found_urls = url_pattern.findall(text)
            urls.extend(found_urls)
            
            links = page.get_links()
            for link in links:
                uri = link.get('uri')
                if uri:
                    urls.append(uri)
        
        images = convert_from_path(self.pdf_path)
        for image in images:
            text_from_image = pytesseract.image_to_string(image)
            found_urls_in_image = url_pattern.findall(text_from_image)
            urls.extend(found_urls_in_image)
        
        urls = list(set(urls))

        if save:
            with open(self.output_txt_path, 'w') as output_file:
                for url in urls:
                    output_file.write(url + '\n')

        return urls
    
    def extract_domains(self, save: bool = False) -> list:
        """
        Extracts URLs and domains from the given PDF file and saves them to the specified text file.
        
        The method extracts URLs and domains from:
        - Text content of each page in the PDF.
        - Hyperlinks in each page of the PDF.
        - Text extracted from images within the PDF.

        URLs and domains found are written to the output text file, with one URL/domain per line.
        """
        if not os.path.exists(self.pdf_path):
            print(f"File not found: {self.pdf_path}")
            return None
        
        pdf_document = fitz.open(self.pdf_path)
        
        # Regular expression to find URLs and domains
        domain_pattern = re.compile(
            r'((?:https?://)?(?:www\.)?[\w-]+\.[\w\.-]+(?:\.[\w\.]{2,})?)'
        )
        
        domains = []

        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            
            text = page.get_text()
            
            found_domains = domain_pattern.findall(text)
            domains.extend(found_domains)
            
            links = page.get_links()
            for link in links:
                uri = link.get('uri')
                if uri:
                    domains.append(uri)
        
        images = convert_from_path(self.pdf_path)
        for image in images:
            text_from_image = pytesseract.image_to_string(image)
            found_domains_in_image = domain_pattern.findall(text_from_image)
            domains.extend(found_domains_in_image)
        
        domains = list(set(domains))

        if save:
            with open(self.output_txt_path, 'w') as output_file:
                for domain in domains:
                    output_file.write(domain + '\n')

        return domains
