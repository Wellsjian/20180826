#!/bin/bash

#编写1个nginx的启动脚本，包含: start stop restart

read -p "请输入您的操作(start|stop|restart|status)" result

case $result in
	"start")
		sudo /etc/init.d/nginx $result
		;;
	"status")
		 sudo /etc/init.d/nginx $result
                ;;
	"stop")
                 sudo /etc/init.d/nginx $result
                ;;
	"restart")
                 sudo /etc/init.d/nginx $result
                ;;
	*)
		echo "Usage: nginx {start|stop|restart|reload|force-reload|status|configtest|rotate|upgrade}
"
esac








