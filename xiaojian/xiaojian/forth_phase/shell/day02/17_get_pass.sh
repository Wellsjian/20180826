#!/bin/bash



key="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm_12345679890"
pass=''
length=${#key}
for i in {1..8}
do
	pass=$pass${key:$[RANDOM%length]:1}
done

echo $pass




