#!/bin/bash


# Install shedskin
#sudo apt-get install shedskin
#sudo apt-get install g++ libpcre++-dev python-all-dev libgc-dev


# Convert Pyton to C++
mkdir bin
cp word_permutation.py bin
cd bin
shedskin word_permutation
make
