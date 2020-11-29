###### 查看docker信息
$ docker version
$ docker-compose --version
$ docker-machine --version
$ docker info

###### 把用户加入docker用户组，避免每次使用sudo
$ sudo usermod -aG docker $USER

###### 运行docker
# service 命令的用法
$ sudo service docker start
$ sudo service docker restart
# systemctl 命令的用法
$ sudo systemctl start docker

###### image镜像管理
# 列出本机的所有 image 文件。
$ docker image ls
# 删除 image 文件
$ docker image rm [IMAGE-ID]
# 如果报错：image has dependent child images 则使用下面命令删除
$ docker rmi -f [REPOSITORY:TAG]
# 查看镜像
$ docker search [REPOSITORY]
# 拉取镜像
$ docker image pull library/hello-world
# 导入镜像
$ docker load < /path/[REPOSITORY].tar.gz
# 导出镜像
$ docker save [REPOSITORY] > /path/[REPOSITORY].tar.gz

###### 容器运行、终止、查看与删除
# 运行容器
$ docker container run hello-world
$ docker container run -it ubuntu bash
# 终止运行容器
$ docker container kill [containID]
# 列出本机正在运行的容器
$ docker container ls
# 列出本机所有容器，包括终止运行的容器
$ docker container ls --all
# 删除容器
$ docker container rm [containerID]

###### 制作容器
$ git clone https://github.com/ruanyf/koa-demos.git
$ cd koa-demos
# 项目根目录创建.dockerignore文件
.git
node_modules
npm-debug.log
# 项目根目录创建Dockerfile文件
FROM node:8.4
COPY . /app
WORKDIR /app
RUN npm install --registry=https://registry.npm.taobao.org
EXPOSE 3000
>>>FROM node:8.4：该image文件继承官方的node image，冒号表示标签，这里标签是8.4，即8.4版本的node
>>>COPY . /app：将当前目录下的所有文件（除了.dockerignore排除的路径），都拷贝进入image文件的/app目录
>>>WORKDIR /app：指定接下来的工作路径为/app
>>>RUN npm install：在/app目录下运行npm install命令安装依赖。注意安装后所有的依赖都将打包进入image文件
>>>EXPOSE 3000：将容器 3000 端口暴露出来，允许外部连接这个端口
# 创建image文件[如果不指定，默认的标签就是latest]
$ docker image build -t koa-demo .
$ docker image build -t koa-demo:0.0.1 .

###### 生成容器
$ docker container run -p 8000:3000 -it koa-demo /bin/bash
$ docker container run -p 8000:3000 -it koa-demo:0.0.1 /bin/bash
# 添加--rm参数，在容器终止运行后自动删除容器文件
$ docker container run --rm -p 8000:3000 -it koa-demo /bin/bash

###### 添加CMD命令
FROM node:8.4
COPY . /app
WORKDIR /app
RUN npm install --registry=https://registry.npm.taobao.org
EXPOSE 3000
CMD node demos/01.js
# 指定了CMD命令以后，docker container run命令就不能附加命令了（比如前面的/bin/bash），否则它会覆盖CMD命令
$ docker container run --rm -p 8000:3000 -it koa-demo:0.0.1

###### 发布image
$ docker login
$ docker image tag [imageName] [username]/[repository]:[tag]
$ docker image tag koa-demos:0.0.1 ruanyf/koa-demos:0.0.1
$ docker image build -t [username]/[repository]:[tag] .
$ docker image push [username]/[repository]:[tag]

###### 其他命令
# docker container run命令是新建容器，每运行一次，就会新建一个容器。同样的命令运行两次，就会生成两个一模一样的容器文件。如果希望重复使用容器，就要使用docker container start命令，它用来启动已经生成、已经停止运行的容器文件
$ docker container start [containerID]
# 前面的docker container kill命令终止容器运行，相当于向容器里面的主进程发出 SIGKILL 信号。而docker container stop命令也是用来终止容器运行，相当于向容器里面的主进程发出 SIGTERM 信号，然后过一段时间再发出 SIGKILL 信号。这两个信号的差别是，应用程序收到 SIGTERM 信号以后，可以自行进行收尾清理工作，但也可以不理会这个信号。如果收到 SIGKILL 信号，就会强行立即终止，那些正在进行中的操作会全部丢失
$ bash container stop [containerID]
# docker container logs命令用来查看 docker 容器的输出，即容器里面 Shell 的标准输出。如果docker run命令运行容器的时候，没有使用-it参数，就要用这个命令查看输出
$ docker container logs [containerID]
# docker container exec命令用于进入一个正在运行的 docker 容器。如果docker run命令运行容器的时候，没有使用-it参数，就要用这个命令进入容器。一旦进入了容器，就可以在容器的 Shell 执行命令了
$ docker container exec -it [containerID] /bin/bash
# docker container cp命令用于从正在运行的 Docker 容器里面，将文件拷贝到本机。下面是拷贝到当前目录的写法
$ docker container cp [containID]:[/path/to/file] .

###### 修改image仓库下载地址
$ sudo vi /etc/default/docker
# 最后加上一行
DOCKER_OPTS="--registry-mirror=https://registry.docker-cn.com"
