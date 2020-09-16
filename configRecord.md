Environment: CentOS7/8


## 1. 打开fastest mirror功能(仅centos8，可选)
```
vi /etc/dnf/dnf.conf
fastestmirror=True
sudo dnf clean all
sudo dnf makecache
```


## 2. 安装docker

```
sudo yum install -y yum-utils  device-mapper-persistent-data  lvm2
sudo yum-config-manager  --add-repo   https://download.docker.com/linux/centos/docker-ce.repo
yum install https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm
sudo yum install docker-ce docker-ce-cli
```

```
启动，验证版本
sudo systemctl start docker
docker --version

开机启动
systemctl enable docker.service
systemctl start docker.service
```


## 3. 拉取镜像
```
docker pull airzihao/aipm:aipm_web0.1  #网速问题，最好直接scp

导入镜像
docker import aipm_web_01.tar
创建容器
docker  run  -ditp 8081:8081  --name=aipmv0.1_base  镜像id  /bin/bash
进入容器
docker exec -it aipmv0.1_base /bin/bash

cd /home/aipm-web
nohup python3 manage.py runserver 0.0.0.0:8081 &
```

## 测试
```
浏览器访问该机器的8081端口
```






## 创建新镜像（!!!若需要）
```
docker内操作：

yum换源：
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
cd /etc/yum.repos.d/
curl -O http://mirrors.163.com/.help/CentOS7-Base-163.repo
mv CentOS7-Base-163.repo CentOS-Base.repo
yum clean all
yum makecache

安装python3.6.5：
yum -y install wget
wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
mv Python-3.6.5.tgz /usr/local
cd /usr/local
tar -xvzf Python-3.6.5.tgz
cd Python-3.6.5
yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-devel  -y
yum -y install gcc automake autoconf libtool make
./configure   
make
make install

换pip3源
mkdir ~/.pip
vi ~/.pip/pip.conf
[global]
index-url = https://mirrors.aliyun.com/pypi/simple

yum install -y git

git clone https://github.com/cas-bigdatalab/aipm-web.git
配置aipm-web:

pip3 install django==2.1.8
pip3 install cmake
yum install gcc-c++ -y
yum -y install boost-devel
pip3 install boost
pip3 install dlib==19.6.1
pip3 install numpy
pip3 install Pillow
pip3 install hyperlpr==0.0.1
pip3 install keras
pip3 install tensorflow
pip3 install matplotlib
pip3 install python_speech_features
pip3 install jieba


yum install libSM-1.2.2-2.el7.x86_64 --setopt=protected_multilib=false
yum install libXrender.x86_64 -y
yum install libXext-1.3.3-3.el7.x86_64 -y
```