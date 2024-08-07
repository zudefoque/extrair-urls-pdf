import argparse
from lemonpdf.__main__ import Extractor

def main():
    
    parser = argparse.ArgumentParser(description='Extract URLs from a PDF file.')
    
    # Add arguments for the CLI
    parser.add_argument('pdf_path', type=str, help='Path to the input PDF file.')
    parser.add_argument('--output', type=str, help='Path to the output text file.', default=None)
    parser.add_argument('--save', action='store_true', help='Save extracted URLs to a text file.')

    # Parse the arguments
    args = parser.parse_args()
    
    # Create an instance of the Extractor class
    extractor = Extractor(pdf_path=args.pdf_path, output_txt_path=args.output)
    
    # Extract URLs and optionally save them to a file
    urls = extractor.extract_urls_from_pdf(save=args.save)
    
    # Display the extracted URLs if not saving to a file
    if not args.save and urls:
        for url in urls:
            print(url)

if __name__ == '__main__':
    main()
