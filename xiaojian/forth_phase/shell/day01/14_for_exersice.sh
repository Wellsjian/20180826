#!/bin/bash

for num in {2..255}
do
	ip=172.40.74.$num
	ping -c 1 $ip &> /dev/null
	if [ $? -eq 0 ];then
		echo "$ip online"
	else
		echo "$ip notonline"
	fi
done


