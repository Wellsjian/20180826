#!/bin/bash

#把把172.40.91.10-15内不在线的IP输出来

num=10
until [ $num -gt 15 ] 
do
	ip="172.40.74.$num"
	ping -c 2 $ip &> /dev/null
	if [ $? -eq 1 ];then
		echo "$ip  可以上线"
	fi
	let num++

done





