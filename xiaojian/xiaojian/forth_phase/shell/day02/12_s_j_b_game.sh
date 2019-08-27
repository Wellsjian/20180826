#!/bin/bash

while :
do
	#电脑随机出拳
	game=('石头' '剪刀' '布')
	computer=${game[$[RANDOM%3]]}
	
	#人的出拳
	echo "------------------------"
	echo "         1.石头         "
	echo "------------------------"
	echo "         2.剪刀         "
	echo "------------------------"
	echo "         3.布           "
	read -p "请出拳(1|2|3):" you
	echo "------------------------"
	echo "------------------------"

	#做出判断
	case $you in
		"1")
			if [ $computer == "石头" ];then
				echo "平局"
			elif [ $computer == "剪刀 "];then
				echo "你赢"
				exit
			else
				echo "计算机赢"
			fi
		  	;;
		"2")
			if [ $computer == "石头" ];then
				echo "计算机赢"
			elif [ $computer == "剪刀" ];then
				echo "平局"
			else
				echo "你赢"
				exit
			fi
			;;
		"3")
			if [ $computer == "石头" ];then
				echo "你赢"
				exit
			elif [ $computer == "剪刀" ];then
				echo "计算机赢"
			else
				echo "平局"
			fi
			;;
		*)
			echo '输入错误'
	esac
done


