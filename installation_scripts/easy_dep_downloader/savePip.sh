#! /bin/bash

read -p "pip_pkg: " pkg
echo "pip install ${pkg}" >> pipDEPList.txt
