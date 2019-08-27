#!/bin/bash

#电脑生成随机数字
computer=$[RANDOM%10000+1]

#游戏者输入数字
for i in {1..30}
do
	read -p 请输入猜谜数字 num 
	if [ $computer -eq $num ];then
		echo "猜对了"
		exit
	elif [ $computer -gt $num ];then
		echo "猜小了"
	elif [ $computer -lt $num ];then
		echo "猜大了"
	else
		echo "请输入合法数字"
	fi
done



