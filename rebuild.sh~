#!/bin/bash

rm -rf ../museum-lod-pages/*
cd scripts
python ./mk_examples.py
cd ..
git add -A .
git commit -m "auto-update" 
git push
hyde gen
