#!/bin/bash

# Regenerate from scratch
rm -rf .site/*

# Clear any old example copies
#rm content/example/activity/*
#rm content/example/concept/*
#rm content/example/group/*
#rm content/example/identifier/*
#rm content/example/legal/*
#rm content/example/name/*
#rm content/example/object/*
#rm content/example/person/*
#rm content/example/place/*
#rm content/example/set/*
#rm content/example/text/*
#rm content/example/value/*
#rm content/model/example_index.html

# Remake the table, still separate
#python scripts/mk_table.py

# Split up the current ontology into little static files
#rm content/ns/terms/*
#python scripts/split_ontology.py

# And now generate the site from scratch
mkdocs build --clean
# Once more incrementally to catch the new index file we built
# RDP ??
mkdocs build
