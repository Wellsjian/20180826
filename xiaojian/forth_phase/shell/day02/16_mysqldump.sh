#!/bin/bash

user='root'
passeord='123456'
dbname='mysql'
date=$(date +%y-%m-%d )



dir="/home/tarena/materials/xiaojian/forth_phase/shell/backup/"

[ ! -d $dir ] && mkdir $dir

mysqldump -u$user -p$password $dbname > $dir$dbname-${date}.sql
















