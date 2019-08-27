#!/bin/bash

# 1、依次提示用户输入3个整数，脚本根据数字大小依次排序输出 3个数字

read -p "请输入第一个整数:" number1
read -p "请输入第二个整数:" number2
read -p "请输入第三个整数:" number3


#保证number1最小. number3最大
if [ $number1 -ge $number2 ];then
	number=$number1
	number1=$number2
	number2=$number
fi
if [ $number1 -ge $number3 ];then
	
	number=$number1
	number1=$number3
	number3=$number
fi

#判断number2 和 number3 的大小
if [ $number2 -ge $number3 ];then
	number=$number2
	number2=$number3
	number3=$number
fi

echo $number1 $number2 $number3


























