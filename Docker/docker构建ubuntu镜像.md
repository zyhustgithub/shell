$ docker pull ubuntu:16.04
$ docker run -it --name myubuntu ubuntu:16.04 bash
$ apt-get update
$ apt-get install vim
$ mv /etc/apt/source.list /etc/apt/source.list.bak
$ vi /etc/apt/source.list
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
$ apt-get update
$ apt-get upgrade
$ apt-get install openssh-server
$ vi /etc/ssh/sshd_config
PermitRootLogin yes # 可以登录 root 用户
PubkeyAuthentication yes # 可以使用 ssh 公钥许可
AuthorizedKeysFile  .ssh/authorized_keys # 公钥信息保存到文件 .ssh/authorized_keys 中
$ /etc/init.d/ssh restart
$ mkdir ~/.ssh
$ touch ~/.ssh/authorized_keys
# 在主机用命令cat ~/.ssh/id_rsa.pub将复制的公钥粘贴到~/.ssh/authorized_keys
$ exit [或者ctrl + d退出容器]
$ docker commit -m 'add openssh' -a 'zengyong' [containerId] myubuntu-ssh
$ docker run -d -p 8888:22 --name ubuntu-ssh myubuntu-ssh /usr/sbin/sshd -D
# 在主机用ssh -p 8888 root@localhost登陆docker容器
# 在主机vi ~/.ssh/config
# Host myubuntu-ssh
#     HostName localhost
#     User     root
#     Port     8888
#     IdentityFile ~/.ssh/id_rsa
# 在主机用ssh myubuntu-ssh免密登陆
