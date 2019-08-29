# **shell_day01_回顾**

- **变量**

```shell
#  = 左右两侧不能有空格
1、自定义变量 : name="蔡依林"
2、环境变量   : $USER $PWD
3、位置变量   : $1 $2 $3 
4、预定义变量 : $# $* $?-->0或者1
```

- **算术运算命令**

```shell
1、`expr n1 + n2`
2、$[n1+n2]
3、let i++
```

- **条件判断**

```shell
 # [ 条件 ]
 1、字符比较:  ==  !=  -z
 2、数值比较:  -gt -ge -lt -le -eq
 3、文件|目录比较: -e !-e -f -d 
   # 文件|目录不存在满足条件
   if [ !-e $directory ]: 
```

- **if分支结构**

```shell
if [ 条件 ];then
	语句
elif [ 条件 ];then
	语句
else
	语句
fi
```

- **for循环**

```shell
# for
for 变量名 in `seq {1..5}`
do
	循环体
done

# cfor
for ((i=1;i<=10;i++))
do
	循环体
done
```

- **while循环**

```shell
while [ 条件 ]
do
	循环体
done

# 死循环
while :
do
	循环体
done
```

- **sed**

```shell
# 查询添加 -n 参数,屏蔽终端调试输出,否则输出两遍
sed -n '' file.txt
# 增删改替换一定加-i参数,对文件内容进行实质性更改
sed -i '' file.txt

1、增   : a | i
2、删   : d
3、改   : c
4、查   : p
# s/原内容/新内容/g g表示全局,否则每行只替换第1个
5、替换 : s  
```

- **其他**

```shell
1、获取随机数 
  $RANDOM
  $[RANDOM%num]
  # $[RANDOM%5] --> 0 1 2 3 4
  # $[RANDOM%5+1]  --> 1 2 3 4 5
```

# **shell_day02_笔记**

- **作业**

**用户从终端输入名字，创建该目录，回车直接退出**

```shell
#!/bin/bash

while :
do
	read -p "请输入要创建的目录(直接回车退出):" dirname
	directory="/home/tarena/$dirname"

	if [ -z $dirname ];then
	    echo "程序退出"
	    exit

	elif [ -e $directory ];then
	    echo "$directory已存在"
	else
	    mkdir $directory
	    echo "$directory创建成功"
	fi
done
```



- **until循环**

```shell
# 1、特点
条件判断不成立时执行循环体,成立时循环结束

# 2、语法格式
until [ 条件 ]
do
	循环体
done

# 3、示例:把172.40.91.10-15内不在线的IP输出来
#!/bin/bash

x=10
# 条件成立,结束!
until [ $x -gt 15 ]
do
    ping -c 2 172.40.91.$x &> /dev/null
    if [ $? -eq 1 ];then
        echo "172.40.91.$x 不在线"
	let x++
    fi
done
```

- **case分支结构**		

```shell
# 1、特点
根据变量值的不同,执行不同的操作

# 2、语法格式
case $变量名 in
模式1)
	代码块 
	;;
模式2)
	代码块
	;;
*)
	代码块
	;;
esac

# 3、示例 : 输入一个字符,判断是数字、字母还是其他字符
#!/bin/bash

read -p "请输入一个字符:" char

# 判断用户输入是否为一个字符
if [ ${#char} -ne 1 ];then
    echo "你输入的不是一个字符!"
    exit
fi

case $char in
    [0-9])
        echo "$char 是一个数字";;
    [a-Z])
	    echo "$char 是一个字母";;
    *)
	    echo "$char 是一个特殊字符";;
esac

# 4、练习 : 编写1个nginx的启动脚本，包含: start stop restart

请输入你的操作(start|stop|restart):
如果用户输入不正确,则提示:
Useage Please input start|stop|restart!
# 代码实现
#!/bin/bash

read -p '请选择操作(start|stop|restart):' choice
case $choice in
    "start")
	    sudo /etc/init.d/nginx start
	    ;;
    "stop")
	    sudo /etc/init.d/nginx stop
	    ;;
    "restart")
	    sudo /etc/init.d/nginx restart
	    ;;
    *)
	    echo "Useage:Please input start|stop|restart!"
	    ;;
esac
```

**知识点总结**

```shell
# 1、获取字符串长度
${#变量名}
name="Lucy"
echo ${#name}  # 结果: 4

# 2、字符串索引及切片
${string:index:number} # number为取元素的数量
key='ABCDE'
${key:0:1} # A 获取下表索引为0的元素
${key:1:2} # BC

# 3、vim批量缩进
1、进入命令行模式 : shift + :
2、1,3> + Enter  : 1-3行缩进
3、1,3< + Enter  : 1-3行往回缩进
```

- **函数**

  **补充一点点Linux命令**

  ```shell
  
  ```


```shell
# 1、语法格式
函数名(){
	代码块
}
函数名  # 函数调用,不能加()

# 2、示例: 打印10个*
star(){
	echo "**********"
}
star # 第1次调用
star # 第2次调用

# 3、练习: 写1个计算器程序,计算 加 减 即可 -- 函数+case

```

**Python字典实现类似于case语句**

```python
#!/usr/bin/env python3

def add_info():
    print('I am add_info')

def modify_info():
    print('I am modify_info')

def delete_info():
    print('I am delete_info')

menu = '''1. 添加学生信息
2. 修改学生信息
3. 删除学生信息
请选择(1/2/3):'''
choice = input(menu).strip()

if choice in ['1','2','3']:
    # 定义一个字典,key为选择,value为对应函数名
    cmd_dict = {
        '1' : add_info,
        '2' : modify_info,
        '3' : delete_info
    }
    # 函数名()
    cmd_dict[choice]()
else:
    print('无效的选择')
```

**练习**

```shell
在用户主目录下创建一个目录,如果存在则提示,否则提示创建成功
#!/bin/bash
  
makedir(){
    read -p "请输入目录名:" dirname
    directory="/home/tarena/$dirname"
    if [ -e $directory ];then
        echo $directory 已存在
    else
        mkdir $directory
        echo 创建成功   
    fi
}

makedir
```

- **字符串处理 - ${变量名  替换符号 匹配条件}**

**从左向右删除**

```shell
# 1、语法
${变量名##匹配条件}

# 2、示例
directory="/home/tarena/mysql"   # 注意{}中不需要加空格
echo ${directory##*/}   --> mysql
echo ${directory#*/}    --> home/tarena/mysql
```

**从右向左删除**

```shell
# 1、语法
${变量名%%匹配条件}

# 2、示例
directory="/home/tarena/mysql"
echo ${directory%%/mysql}   --> /home/tarena
echo ${directory%/*}        --> /home/tarena
echo ${directory%%/*}       --> ""
```

**案例**

```shell
# 1、输出系统中的前10个用户

方法1:
#!/bin/bash
# root:x:0:0:root:/root:/bin/bash
for line in `head -10 /etc/passwd`
do
    echo ${line%%:*}
done

方法2: awk
# root:x:0:0:root:/root:/bin/bash
awk -F ':' '{print $1}' /etc/passwd | head

方法3: sed 's/原内容/新内容/g'
sed 's/:.*//g' /etc/passwd | head
```

**练习**

```shell
批量修改文件名 : 把当前目录下的.txt文件全部改为.doc文件
# 创建10个 .txt 文件
touch file{1..10}.txt

#!/bin/bash
for filename in `ls *.txt`
do
    # file1.txt  -->  file1.doc
    name=${filename%.txt}
    mv $filename $name.doc
done
```

- **shell磨练**

**1、依次提示用户输入3个整数，脚本根据数字大小依次排序输出 3个数字**

```shell
# shell实现
#!/bin/bash

read -p "请输入第一个整数:" n1
read -p "请输入第二个整数:" n2
read -p "请输入第三个整数:" n3

# 1.保证n1是最小值
if [ $n1 -ge $n2 ];then
    temp=$n1 n1=$n2 n2=$temp
fi
if [ $n1 -ge $n3 ];then
    temp=$n1 n1=$n3 n3=$temp
fi
# 2.判断n2和n3
if [ $n2 -ge $n3 ];then
    temp=$n2 n2=$n3 n3=$temp
fi

echo "排序后:$n1 $n2 $n3"

# python
n1 = int(input('第一个:'))
n2 = int(input('第二个:'))
n3 = int(input('第三个:'))

L = [n1,n2,n3]
L.sort()
print(L)
```

**2、编写脚本，实现人机<石头，剪刀，布>游戏** 

```shell
# 提示 - Linux中数组使用
# Linux数组: (元素1 元素2 元素3)  元素之间用空格隔开
game=("石头" "剪刀" "布")
${game[0]}
# 电脑随机出拳
${game[$[RANDOM%3]]}
```

**shell代码实现**

```shell
#!/bin/bash

# 1.电脑出拳
game=("石头" "剪刀" "布")
computer=${game[$[RANDOM%3]]}
# 2.用户出拳
echo "+---------------------+"
echo "+     1.石头          +"
echo "+     2.剪刀          +"
echo "+     3.布            +"
echo "+---------------------+"
read -p "请出拳(1/2/3):" you
# 3.做判断
case $you in
1)
    if [ $computer == "石头" ];then
	echo "平局"
    elif [ $computer == "剪刀" ];then
	echo "你赢"
    else
	echo "计算机赢"
    fi
    ;;

2)
    if [ $computer == "石头" ];then
	echo "计算机赢"
    elif [ $computer == "剪刀" ];then
	echo "平局"
    else
	echo "你赢"
    fi
    ;;
3)
    if [ $computer == "石头" ];then
	echo "你赢"
    elif [ $computer == "剪刀" ];then
	echo "计算机赢"
    else
	echo "平局"
    fi
    ;;
*)
    echo "出拳无效!请输入1/2/3"
    ;;
esac
```

**python代码实现**

```python
#!/usr/bin/env python3
import random

all_list = ['石头','剪刀','布']
win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]
computer = random.choice(all_list)

you = input('1.石头\n2.剪刀\n3.布\n请出拳(1/2/3):')

if all_list[int(you)-1] == computer:
    print('平局')
elif [all_list[int(you)-1],computer] in win_list:
    print('你赢')
else:
    print('计算机赢')
```

**3、每2秒中检测一次MySQL数据库的连接数量**

```shell
# mysqladmin命令
mysql服务器管理任务的工具，它可以检查mysql服务器的配置和当前工作状态

mysqladmin -uroot -p123456 status
```

​	**代码实现**

```shell
#!/bin/bash

while :
do
   count=`mysqladmin -uroot -p123456 status | awk '{print $4}'`
   echo "`date +%F` 并发连接数为: $count"
   sleep 2
done
```

**4、根据md5校验码，检测文件是否被修改**

```shell
# 1、生成md5的文件校验码
md5sum nginx.conf

/etc/*.conf 做md5校验码,md5file.txt

# 2、diff命令: 两个文件找不同
diff 文件1 文件2
# 文件1第30行 change 文件2第30行 
30c30
< 291e59190bb2c52e01fa7fa9ebb2ba01  /etc/test.conf
---
> 7cdda976172d4819ac60401235647806  /etc/test.conf
```

**代码实现**

```shell
#!/bin/bash

for file in `ls /etc/*.conf`
do
    md5sum $file >> md5log2.txt
done
```

**5、备份MySQL数据库**

```shell
# 数据库备份命令
mysqldump -hIP -uroot -p123456 库 > xxx.sql
```

**代码实现**

```shell
#!/bin/bash

user="root"
password="123456"
dbname="mysql"
date=$(date +%Y%m%d)

# ! 和 -d之间要加空格
[ ! -d /home/tarena/backup ] && mkdir /home/tarena/backup

mysqldump -u"$user" -p"$password" "$dbname" > /home/tarena/backup/"$dbname"-${date}.sql
```

**6、随机生成8为密码-字母、数字、__**

```shell
# 1.获取字符串长度: ${#变量名}
# 2.字符串索引切片: ${变量名:起始索引:1}
key=''
length=${#key}
${key:$[RANDOM%length]:1}
```

代码实现

```shell
#!/bin/bash
  
key='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM_'
length=${#key}

pass=''
for i in {1..8}
do
    pass=$pass${key:$[RANDOM%length]:1}
done

echo $pass
```















