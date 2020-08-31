# aipm-web
This is the aipm-web project.

## Requirement
```
Centos 7 or later relese edition.
Docker 19.03.12 or later
```

## Deployment
```
1. docker (if needed)
sudo yum install -y yum-utils  device-mapper-persistent-data  lvm2
sudo yum-config-manager  --add-repo   https://download.docker.com/linux/centos/docker-ce.repo
yum install https://download.docker.com/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm
sudo yum install docker-ce docker-ce-cli

2. pull the image
docker pull airzihao/aipm:aipm_web0.1  #The cost time depends on your network env, may takes several minutes.
docker run -ditp 8081:8081 airzihao/aipm:aipm_web0.1 /bin/bash
docker exec -it $container_id /bin/bash

3. exec in the container
cd /home/aipm
nohup python3 manage.py runserver 0.0.0.0:8081
```
Details about install and deployment, go to https://github.com/cas-bigdatalab/aipm-web/blob/master/configRecord.md