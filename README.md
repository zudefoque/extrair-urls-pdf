# lemonpdf

![PyPI - Downloads](https://img.shields.io/pypi/dm/lemonpdf)
![PyPI - License](https://img.shields.io/pypi/l/lemonpdf)
![GitHub Tag](https://img.shields.io/github/v/tag/JuanBindez/lemonpdf?include_prereleases)
<a href="https://pypi.org/project/lemonpdf/"><img src="https://img.shields.io/pypi/v/lemonpdf" /></a>

### Python3 library to get urls from PDF files.


### Install
    sudo apt install tesseract-ocr poppler-utils
    pip install lemonpdf

### Quickstart


### Command line interface use (CLI)

#### get urls

    lemonpdf -u file.pdf

#### save urls list in file txt

    lemonpdf -u file.pdf -o urls.txt -s

#### get domains

    lemonpdf -d file.pdf

#### save domains in file txt

    lemonpdf -d file.pdf -o domains.txt -s

### scripts

#### get urls and save file txt

```python

from lemonpdf import Extractor

pdf_path = 'file.pdf'
output_txt_path = 'out_file.txt'

extractor = Extractor(pdf_path=pdf_path, output_txt_path=output_txt_path)

urls = extractor.extract_urls_from_pdf(save=True)

print(urls)


```

#### get domains and save file txt

```python
from lemonpdf import Extractor

pdf_path = 'file.pdf'
output_txt_path = 'domains.txt'

extractor = Extractor(pdf_path=pdf_path, output_txt_path=output_txt_path)

urls = extractor.extract_domains_from_pdf(save=True)

print(urls)


```