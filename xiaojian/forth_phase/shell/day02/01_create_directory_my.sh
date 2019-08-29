#!/bin/bash


dir="/home/tarena/materials/xiaojian/forth_phase/shell"
while :
do
	read -p 请输入要创建的目录(直接回车退出): dirname
	directory="$dir/$dirname"
	if [ -z $dirname ];then
		echo "程序退出"
		exit
	elif [ -e $directory ];then
	echo "该路径已经存在"
	else
	mkdir $directory
	echo "$directory  已经创建成功"
	exit
	fi
done
