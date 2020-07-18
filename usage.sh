#!/bin/bash
set -e

:<<MULTILINE-NOTE
    LINUX SHELL
    相关用法
MULTILINE-NOTE

echo "-------------------------------------------"
# 文件包含
source extend.sh
# . ./extend.sh
echo ${HEADER_PATH}

echo "-------------------------------------------"
# 标准输入和打印函数及重定向
read -p "Please input two words:" -n 12 -t 10 -s input1 input2 <<INBUF
str 123.123
INBUF
printf "input1=%-10s input2=%-4.2f\n" ${input1} ${input2}
# 2> 错误，2>> 追加错误，&> 错误和正确
# 2>&1 错误重定向到标准输出[&0 标准输入，$1 标准输出，$2 标准错误，/dev/nul，文件]
# cat < input.txt > output.txt

echo "-------------------------------------------"
# 传递参数
echo 参数个数: $#
echo 全部参数: '$@='$@ 或者 '$*='$*
echo '$@与$*的区别在于加双引号时，\"$\"所有参数会被整个当作一个字符串'
for arg in "$*"; do
    echo $arg
done
for arg in "$@"; do
    echo "$arg"'\\n'" \c"
done
echo "\n\c"
echo 脚本当前进程ID: $$
echo 后台运行最后一个进程ID: $!
echo 命令退出状态值: $?
echo shell当前使用的选项: $-

echo "-------------------------------------------"
# 定义变量
ROOT_PATH=$(cd $(dirname $0) && pwd)
echo "当前脚本所在目录[\"${ROOT_PATH}\"]"
readonly ROOT_PATH                                                # 只读变量，不能unset删除
# unset ROOT_PATH                                                 # 删除变量

echo "-------------------------------------------"
# 字符串
myName=zengyong
echo 双引号拼接: "${myName} $myName"
echo 单引号拼接: '${myName} $myName '${myName}' '$myName''          # 单引号拼接需注意
echo 字符串长度: '${#myName}='${#myName}''
echo 字符串子串: '${myName:0:4}='${myName:0:4}''
echo 查找字符串: $(awk -v a="${myName}" -v b="yong" 'BEGIN{print index(a,b)}')

echo "-------------------------------------------"
# 数组
array=(little middle)
array[0]=small                                                    # 单个赋值，并覆写
array[2]=large
echo '${#array[@]}='"${#array[@]}" '${#array[*]}='"${#array[*]}"  # 获取数组大小
for elem in ${array[*]}; do                                       # ${array[@|*]表示获取所有元素
    echo '${elem}='${elem} '${#elem}='${#elem}                    # ${#elem}获取元素大小
done

echo "-------------------------------------------"
# 关系运算符：-eq -ne -lt -gt -le -ge
# 布尔运算符：非 ! 或 -o 且 -a
# 逻辑运算符：&& ||
# 字符串运算符：= != -z(字符串长度为0返回true) -n(字符串长度不为0返回true) $字符串为空返回true
unset myName
myName="zeng yong"
if [ -n "${myName}" -a "${myName}" = "zeng yong" ]; then
    echo "It's true | \c"
fi
# 注意使用逻辑运算符时是两个中括号，且不能使用布尔运算符 -a 和 -o
if [[ -n "${myName}" && ! -z "${myName}" && "${myName}" = "zeng yong" ]]; then
    echo "It's true | \c"
fi
# 文件描述符 -d -f -x -r -w ...
if [ -d ${ROOT_PATH} ]; then
    echo "Dir exist."
fi

echo "-------------------------------------------"
# 循环
# for file in $(ls /Users/zengyongFamily/Desktop/日常编码); do
#     echo ${file}
# done
for drink in Milk Water Wine; do
    echo "${drink} | \c"
done
echo "\n\c"

echo "-------------------------------------------"
# 函数
function LOG() {
    printf "$*\n"   # 注意上面提到的加引号时"%@"和"&*"的区别
}
LOG Hello, Zeng Yong!

echo "-------------------------------------------"
# 流程控制 for while until case
# break 跳出所有循环，continue 跳出当前循环
for (( ; ; )) # 死循环while : 或 while true
do
    echo -n "输入1-5之间的数字:"
    read aNum
    case $aNum in
        1|2|3|4|5) echo "输入的数字为:${aNum}"
        ;;
        *) echo "输入无效"
            break # continue 会死循环
        ;;
    esac
done