#!/bin/bash

while :
do
	count=`mysqladmin -uroot -p123456 status | awk '{print $4}' `
	echo "`date +%F` 并发连接数为: $count"
	sleep 2
done












