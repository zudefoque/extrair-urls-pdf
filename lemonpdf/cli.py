import argparse
from lemonpdf.__main__ import Extractor

def main():
    parser = argparse.ArgumentParser(description='Extract URLs or domains from a PDF file.')
    
    # Add mutually exclusive group for -u (urls) and -d (domains)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', action='store_true', help='Extract URLs from the PDF.')
    group.add_argument('-d', action='store_true', help='Extract domains from the PDF.')
    
    # Add arguments for the CLI
    parser.add_argument('pdf_path', type=str, help='Path to the input PDF file.')
    parser.add_argument('-o', '--output', type=str, help='Path to the output text file.', default=None)
    parser.add_argument('-s', '--save', action='store_true', help='Save extracted URLs/domains to a text file.')

    # Parse the arguments
    args = parser.parse_args()
    
    # Create an instance of the Extractor class
    extractor = Extractor(pdf_path=args.pdf_path, output_txt_path=args.output)
    
    # Extract URLs or domains based on the user's choice
    if args.u:
        extracted_data = extractor.extract_urls(save=args.save)
    elif args.d:
        extracted_data = extractor.extract_domains(save=args.save)

    # Display the extracted URLs/domains if not saving to a file
    if not args.save and extracted_data:
        for item in extracted_data:
            print(item)

if __name__ == '__main__':
    main()
