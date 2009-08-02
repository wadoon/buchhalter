#!/bin/bash 

m=__init__.py

for i in *.ui
do
	b=${i%%.*}
	echo ${b}.ui > ${b}.py
	pyuic4 -o ${b}.py $i
	echo "from $b import " '*'
	echo  "from $b import " '*' >> $m
done

rm *.pyc




