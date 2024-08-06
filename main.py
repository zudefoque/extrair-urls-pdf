from pdfurls import Extractor

pdf_path = 'arquivo.pdf'
output_txt_path = 'arquivo.txt'

extractor = Extractor(pdf_path=pdf_path, output_txt_path=output_txt_path)

urls = extractor.extract_urls_from_pdf(save=True)

print(urls)
