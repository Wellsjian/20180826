#!/bin/bash

# shell位置变量

echo $1

echo $2

echo $3 #... ... shell的位置变量

echo $4

# 预定义变量

echo $#  : #返回命令行的参数个数

echo $*  : #返回命令行的所有参数

echo $?

# $? : 返回上一条命令执行的状态(0代表正确,非0代表失败)
