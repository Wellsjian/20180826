#!/bin/bash


#方法一
#for line in `head -10 /etc/passwd`
#do
#	echo ${line%%:*}
#done


#方法二
#head -10 /etc/passwd | awk -F ":" '{print $1}'


#方法三

#sed "s/:.*//g" /etc/passwd | head -10 



