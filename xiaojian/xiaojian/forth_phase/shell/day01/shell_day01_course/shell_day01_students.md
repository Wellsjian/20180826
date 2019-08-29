# **shell编程 - Day01笔记**

- **Shell格式**

```shell
# 解释器: bash 、sh
1、扩展名: xxx.sh
2、正文第一行必须指定解释器: #!/bin/bash
```

-  **shell执行方式**

```shell
# 方式一: 加权限,  ./xxx.sh 执行
1、chmod +x  xxx.sh
2、./xxx.sh

# 方式二: 手动指定解释器
bash xxx.sh
```

- **自定义变量**

```shell
# 1. 定义变量
变量名=值    ---->  注意: =两侧绝对不能有空格
eg1: name="take me to your heart"

# 2. 调用变量的格式
echo $变量名

# 01_variable_1.sh
name="风云雄霸天下"
echo $name
     
# 3. 小细节: 单引号和双引号的区别
单引号: 无法获取变量的值
双引号: 可以获取变量的值
```

- **环境变量+位置变量+预设变量**

```shell
tarena :    x    :  1000  :  1000 : 
用户名   密码占位符    UID      GID
tarena,,,:  /home/tarena : /bin/bash
用户描述      主目录/家目录     登录权限

# 环境变量
echo $USER   --  当前用户
echo $UID    --  当前用户的UID号
echo $PWD    --  当前路径
echo $PATH   --  命令搜索路径

# python位置变量: sys.argv
  sys.argv --> 列表
  sys.argv[0] --> py文件名
  sys.argv[1] --> 第1个命令行参数
  sys.argv[2] --> 第2个命令行参数
# shell位置变量  ./xxx.sh 1 2
$1 $2 $3 ... ... shell的位置变量

# 预定义变量
$# $* $?

# $? : 返回上一条命令执行的状态(0代表正确,非0代表失败)

# 示例代码: ./03_argv.sh 1 2 3 4
#!/bin/bash
  
echo $1  --> 1
echo $2  --> 2
echo $3  --> 3
echo $4  --> 4

echo $#  --> 4 # 获取参数个数
echo $*  --> 1 2 3 4 # 获取所有参数
echo $?  --> 0 # 上面1条命令的执行状态,0成功
```

**练习**

```shell
输出$1+$2,例如输出结果: 3+5
#!/bin/bash
echo $1+$2
```

- **变量赋值 - 接收用户从终端输入的值**

```shell
# 语法格式
read -p 提示信息 变量名

# 05_read.sh
#!/bin/bash
read -p 请输入姓名: name
echo "您输入的姓名是:$name"

# 指定超时时间
read -p 提示信息 变量名
read -t n -p 提示信息 变量名

# 06_read_t.sh 限制3秒中之内必须输入值
#!/bin/bash
read -t 3 -p 请输入用户名: username
```

**练习**

```shell
1、输入学生姓名: 赵敏
2、输入学生成绩: 88
3、输出: 赵敏的成绩为88分
#!/bin/bash
read -p "输入学生姓名:" name
read -p "输入学生成绩:" score
echo "$name的成绩为$score分"
```

**Ubuntu设置sudo免密码**

```shell
# 通过更改 /etc/sudoers 实现
1、备份: sudo cp /etc/sudoers .
2、修改: sudo vi /etc/sudoers
   添加: tarena ALL=(ALL) NOPASSWD : ALL
```

**练习**

```shell
请使用位置变量的方式实现用户名的创建
#!/bin/bash
sudo useradd $1
echo "$1创建成功"
运行: ./xxx.sh tom

# 创建用户: useradd 用户名
# 删除用户: userdel 用户名
```

- **shell - 算术运算符**

```shell
# 运算符
1、+ - * / %
2、++ : 自加1运算,类似于python中 i+=1
3、-- : 同++
			
# 运算命令
1、let 运算表达式
	i=1
	let i++
	echo $i
2、expr 运算表达式
	i=1
	sum=`expr $i + 5` # +两侧要有空格
	echo $sum
3、$[]
	echo $[1+1]
	echo $[1-1]
	echo $[a+a] # 调用变量不用多次添加$符号
	echo $[1*1] # 乘法无需转义
	echo $[$1+$2+$3]
```

**练习**

```shell
使用 位置变量+以上方法一、二中任何一种,实现2个数字的相加
#!/bin/bash
echo $[$1+$2]
echo `expr $1 + $2`
```

- **shell - 比较运算符**

```shell
# 语法格式
 [  判断语句  ]      # 注意括号必须有空格
# 组合
&& 并且  --> python中 and
|| 或者  --> python中 or

A命令  &&  B命令   //仅当A成功时才执行B
A命令  ||  B命令   //仅当A失败时才执行B

思考: [ a == a ] && echo Y || echo N 代表什么意思？

# 1、字符比较
[ A == A ]    # 相等(等号两边需要有空格)
[ A != B ]    # 不相等
[ -z $变量 ]   # 判断是否为空
思考(Y 还是 N):  [ $USER == tarena ] && echo Y || echo N

练习: 用户输入用户名,判断是否为空,不为空时创建,否则直接退出程序

#!/bin/bash
read -p "请输入用户:" username
[ -z $username ] && exit
sudo useradd $username

# 2、数字比较
	-eq	等于(equal)
	-ne	不等于(not equal)
	-gt	大于(greater than)
	-ge	大于等于(great or equal)
	-lt	小于(less than)
	-le	小于等于(less or equal)
思考输出什么:
[ 10 -eq 10 ] && echo Y || echo N
[ 11 -le 10 ] && echo Y || echo N
[ 12 -ge 3 ] && echo Y || echo N

# 3、文件|目录比较
   [ -e 文件或目录 ]    # 是否存在exist
   [ -f  文件 ]        # 存在且为文件file
   [ -d  目录 ]        # 存在且为目录directory
   [ -r 文件或目录 ]    # 判断是否可读read
   [ -w 文件或目录 ]    # 判断是否可写write
   [ -x 文件或目录 ]    # 判断是否可执行
思考输出:
	[ -e /etc/passwd ] && echo Y || echo N
	[ -f /etc/passwd ] && echo Y || echo N
	[ -d /etc/passwd ] && echo Y || echo N
```

**if分支结构**

```shell
# 1、单分支语法格式
     if [ 条件 ];then
        命令
        命令
     fi
# 2、双分支语法格式
	if [ 条件 ];then
		命令1
	else
		命令2
	fi
# 3、多分支语法格式
  if [ 条件 ];then
    命令1
  elif [ 条件 ] ;then
    命令2
  else
    命令3
  fi
# 示例
#!/bin/bash
if [ $USER == tarena ];then
	echo "Yes,You are Tarena."
else
	echo "You are other man."
```

**练习**

```shell
使用shell编写猜数字游戏,无须循环
# 计算机随机出数字: computer=$RANDOM

#!/bin/bash
# 生成1-5之间的随机整数
computer=$[RANDOM%5+1]
echo $computer

read -p "请猜数字:" you

if [ $you -eq $computer ];then
    echo '恭喜,猜对了!'
    exit
elif [ $you -lt $computer ];then
    echo '猜小了'
else
    echo '猜大了'
fi
```

- **for循环**

```shell
# 语法格式
for 变量 in 值序列
do
	命令
done
# 示例1
for i in 1 2 3 4 5
do
	echo "hello world"
done

# 示例2:  {1..5} 从1到5
for i in {1..5}

# 示例3: 执行Linux命令,获取结果,使用 ``
for i in `Linux命令`
```

**造数 - seq**

```shell

```

**练习**

```shell
把猜数字游戏改为for循环，猜测100次

# 练习:判断指定网段的IP地址哪些可以用,哪些不能用？
#!/bin/bash

online=0
down=0

for i in {2..254}
do
    ping -c 1 172.40.74.$i &> /dev/null
    # 判断$?的值
    if [ $? -eq 0 ];then
	echo "172.40.91.$i onLine"
	let online++
    else
	echo "172.40.91.$i Down"
	let down++
    fi
done

echo "Online - $online"
echo "Down - $down"
```



**c-for循环**

```shell
# 语法格式
for ((赋初值;条件;步长))
do
	执行命令
done

# 示例: 打印1-5之间的整数
for ((i=1;i<=5;i++))
do
	echo $i
done
```



- **while循环**

```shell
# 语法格式
while 条件判断
do
	命令
done

# 示例
#!/bin/bash
i=1
while [ $i -le 5 ]
do
   echo $i
   let i++
done

# 死循环:
while :
do
    执行命令
done

# 简陋的计时器
#!/bin/bash
i=1
while :
do
    echo $i
    let i++
    sleep 1
    clear
done
```

**文本处理工具 - sed**

```shell
# 1、定义
非交互式文本编辑器,逐行处理

# 2、语法格式
sed [选项] '条件指令' 文件名
指令: 增删改查

# 查 - p
sed -n 'p' file.txt      # 打印所有内容
sed -n '1p' file.txt     # 打印第1行内容
sed -n '1,3p' file.txt   # 打印1-3行内容
sed -n '1p;3p' file.txt  # 打印1和3行内容

# 删 - d
sed -i '1d' file.txt     # 删除第1行内容
sed -i '$d' file.txt     # 删除最后1行内容
sed -i '1,3d' file.txt   # 删除第1-3行内容
sed -i '1d;3d' file.txt  # 删除第1和第3行内容

# 改 - c
sed -i 'c内容' file.txt   # 修改所有行内容
sed -i '1c内容' file.txt  # 修改第1行内容
sed -i -e '1c李白' -e '3c杜甫' file.txt 
# 修改第1行为李白,修改第3行为杜甫

# 增加 - a i
a: 在当前处理行的下一行插入
i: 在当前处理行的上一行插入
sed -i 'a李白' file.txt  # 每一行的下一行都李白
sed -i '1a李白' file.txt
sed -i '3i杜甫' file.txt

# 增-a 删-d 改-c 查-p

# 替换 - s
sed -i '条件/原内容/新内容/选项' file.txt
选项: g 表示全局替换  i 忽略字母大小写
# 只替换每行中第一个李白
sed -i '1,3s/李白/李清照/' file.txt 
# 替换每行中所有李白,加 g 选项
sed -i '1,3s/李白/李清照/g' file.txt
```

**练习**

```shell
每隔1秒钟,从1个文件中随机取出1行,在大屏幕上显示
# 1. 文件的行数,利用 $RANDOM 想办法取出随机数
  number=$(wc -l file.txt)
  number=$(sed -n '$=' file.txt)
  $[]
# 2. sed -n '随机数p' file.txt

# 代码实现
#!/bin/bash

# 定义常用变量
file="file.txt"
# 1.获取到行数
number=$(sed -n '$=' $file)
# 2.整体逻辑
while :
do
    clear
    n=$[RANDOM%number+1]
    sed -n "${n}p" $file
    sleep 1
done
```

**文件|目录判断示例**

```shell
# 1. 基本判断 - 功能实现
/home/tarena/libai
判断路径是否存在:
不存在: 创建
已存在: 不做操作

# 2. 用户从终端输入要创建的目录名,存在则告知用户,否则帮用户创建此目录
```





