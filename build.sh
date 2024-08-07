#!/bin/bash

git add .
git commit -m 'lemonpdf 1.0.0'
git push -u origin main
git tag v1.0.0
git push --tag
make clean
make upload