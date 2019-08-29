# **shell_day01_回顾**

- **变量**

```shell
#  = 左右两侧不能有空格
1、自定义变量
2、环境变量
3、位置变量
4、预定义变量 : $# $* $?
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
sed -i '' file.txt
sed -n '' file.txt

1、增   : a | i
2、删   : d
3、改   : c
4、查   : p
5、替换 : s
```

- **其他**

```shell
1、获取随机数
  $[RANDOM%num]
```

# **shell_day02_笔记**

- **作业**

**用户从终端输入名字，创建该目录，回车直接退出**

```shell

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
 
```

- **case分支结构**		

```shell
# 1、特点
根据变量值的不同,执行不同的操作

# 2、语法格式
$变量名 in
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


# 4、练习 : 编写1个nginx的启动脚本，包含: start stop restart

```

**知识点总结**

```shell
# 1、获取字符串长度
${#变量名}

# 2、字符串索引及切片
${string:index:number}
key='ABCDE'
${key:0:1} # A 获取下表索引为0的元素
${key:1:2} # BC

# 3、vim批量缩进
1、进入命令行模式 : shift + :
2、1,3> + Enter  : 1-3行缩进
3、1,3< + Enter  : 1-3行往回缩进
```

- **函数**

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

**练习**

```shell
在用户主目录下创建一个目录,如果存在则提示,否则提示创建成功

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
输出系统中的前10个用户

```

**练习**

```shell
批量修改文件名 : 把当前目录下的.txt文件全部改为.doc文件

```

- **shell磨练**

**1、依次提示用户输入3个整数，脚本根据数字大小依次排序输出 3个数字**

```shell

```

**2、编写脚本，实现人机<石头，剪刀，布>游戏** 

```shell
# 提示 - Linux中数组使用
# Linux数组: (元素1 元素2 元素3)  元素之间用空格隔开
game=("石头" "剪刀" "布") 
```

​	**代码实现**

```shell

```

**3、每2秒中检测一次MySQL数据库的连接数量**

```shell
# mysqladmin命令
mysql服务器管理任务的工具，它可以检查mysql服务器的配置和当前工作状态
```

​	**代码实现**

```shell

```

**4、根据md5校验码，检测文件是否被修改**

```shell
# 1、生成md5的文件校验码
md5sum nginx.conf
```

​	**代码实现**

```shell

```

**5、备份MySQL数据库**

```shell

```

**6、随机生成8为密码**

```shell

```







