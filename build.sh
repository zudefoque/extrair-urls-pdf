#!/bin/bash

git add .
git commit -m 'lemonpdf 2.0.0'
git push -u origin main
git tag v2.0.0
git push --tag
make clean
make upload