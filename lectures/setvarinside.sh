#!/usr/bin/bash

for i in `ls -1d Sem*/`; 
do 
	echo $i; 
	cd $i
	git rm logo-python.png  
	git rm logo-tux.png  
	git rm logo-unab.png  
	git rm preamble.tex
	ln -v ../logo-python.png logo-python.png
	ln -v ../logo-tux.png logo-tux.png
	ln -v ../logo-unab.png logo-unab.png
	ln -v ../preamble.tex preamble.tex
	git add .
	git commit -m "update preamble"
	git push
	cd ../
done


