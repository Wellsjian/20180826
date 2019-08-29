#!/bin/bash


#示例 : 输入一个字符,判断是数字、字母还是其他字符

read -p 请输入一个字符: char

#判断输入字符的数量是否符合要求
if [ ${#char} -ne 1 ];then
	echo "输入不正确"
	exit
fi
case $char in
	[0-9])
		echo "$char是一个数字"
		;;
	[a-Z])
		echo "$char是一个字母"
		;;
	*)
		echo "$char是一个特殊字符"
esac


