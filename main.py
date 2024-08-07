from lemonpdf import Extractor

pdf_path = 'tabela.pdf'
output_txt_path = 'domains.txt'

extractor = Extractor(pdf_path=pdf_path, output_txt_path=output_txt_path)

urls = extractor.extract_domains(save=True)

print(urls)
