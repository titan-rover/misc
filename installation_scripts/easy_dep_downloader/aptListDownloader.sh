#! /bin/bash


input="/home/javier/easy_dep_downloader/apt_xavier.txt"
while IFS= read -r line
do
	 sudo apt-get install "${line%%/*}" && echo "${line%%/*}" >> aptlistCommands.txt 
done < "$input"
