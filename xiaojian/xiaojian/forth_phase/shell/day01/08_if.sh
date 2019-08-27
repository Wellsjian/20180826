#!/bin/bash


read -p "请输入用户名:" name

[ -z $name ] && exit
 
sudo useradd ap

