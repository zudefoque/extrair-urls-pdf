#!/bin/bash

git add .
git commit -m 'fix cli'
git push -u origin dev
git tag v1.0-rc9
git push --tag
make clean
make upload