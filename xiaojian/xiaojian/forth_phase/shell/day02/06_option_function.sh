#!/bin/bash

## 3、练习: 写1个计算器程序,计算 加 减 即可 -- 函数+case

read -p "请输入第一个数" num1
read -p "请输入第二个数" num2
read -p "请选择运算符(+-)" op

case $op in
	"+")

		add(){
		echo `expr $num1 + $num2`
		}
		add
		;;
	"-")
		sub(){
		echo `expr $num1 - $num2`
		}
		sub
		;;
	*)
		echo "运算符无效"
esac





