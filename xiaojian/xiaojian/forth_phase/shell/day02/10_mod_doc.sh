#!/bin/bash

for dic in `find /home/tarena/materials/xiaojian/forth_phase/shell/day02 -name '*.txt'`
do
	filename=${dic##*/}
	name=${filename%.txt}
	mv $filename $name.doc
done






