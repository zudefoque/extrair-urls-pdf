#!/bin/bash

git add .
git commit -m 'Add CLI options to extract URLs and domains from PDFs.
 
Implement -u option for URL extraction and -d option for domain extraction, with additional options for saving output to a file
'
git push -u origin dev
git tag v2.0-rc2
git push --tag
make clean
make upload