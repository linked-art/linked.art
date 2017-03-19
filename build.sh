#!/bin/bash

rm -rf .site/*
cd scripts
python ./mk_examples.py
cd ..
hyde gen
