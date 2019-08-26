#!/bin/bash

file="17_sed.txt"
#number=$(wc -l 17_sed.txt)
number=$(sed -n "$=" $file)
while : 
do
        clear
        crow=$[RANDOM%number+1]
        sed -n "${crow}p" $file
        sleep 1
done

