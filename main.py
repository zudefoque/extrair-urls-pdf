from lemonpdf import Extractor

pdf_path = 'file.pdf'
output_txt_path = 'out_file.txt'

extractor = Extractor(pdf_path=pdf_path, output_txt_path=output_txt_path)

urls = extractor.extract_urls_from_pdf(save=True)

print(urls)
