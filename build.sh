#!/bin/bash

# Regenerate from scratch
rm -rf .site/*

# Clear any old example copies
rm content/example/activity/*
rm content/example/group/*
rm content/example/identifier/*
rm content/example/info/*
rm content/example/object/*
rm content/example/person/*
rm content/example/place/*

# Remake the table, still separate
python scripts/mk_table.py

# And now generate the site
hyde gen



