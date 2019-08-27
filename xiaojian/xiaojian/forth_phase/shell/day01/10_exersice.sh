#!/bin/bash


computer=$[RANDOM%5+1]
echo $computer
read -p 请输入数字: number
if [ $computer -eq $number ];then
	echo "猜对了"
	exit
elif [ $computer -lt $number ];then
	echo "猜大了"
else [ $computer -gt $number ]
	echo "猜小了"
fi


