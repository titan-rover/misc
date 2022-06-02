#! /bin/bash
while IFS="" read -r p || [ -n "$p" ]
do
  pip install "$p"
done < pip_xavier.txt

