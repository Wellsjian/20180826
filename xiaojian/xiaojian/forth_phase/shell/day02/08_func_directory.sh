#!/bin/bash

create_dir(){
	read -p "请输入目录名:" dirname
	directory="/home/tarena/materials/xiaojian/forth_phase/shell/day02/$dirname"
	if [ !-e $directory ];then
		mkdir $directory
	else
		echo "文件夹已经存在"
	fi

}

create_dir













