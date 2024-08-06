#!/bin/bash

git add .
git commit -m 'update'
git push -u origin dev
git tag v1.0-rc7
git push --tag
make clean
make upload