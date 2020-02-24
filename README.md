### Flask Docker Scaffold
------
update from Flask Skeleton
添加了Dockerfile 以及 log



------
#### 目录结构

```
├── Makefile
├── manage.py
├── README.md
├── requirements.txt
├── docker
│   ├── ubuntu
│   │   ├── Dockerfile.py # Ubuntu & 安装python3
│   ├── base
│   │   ├── Dockerfile.py # python安装包
│   └── base
│       ├── Dockerfile.py # python安装包
├── appname
│   ├── controllers
│   │   ├── main.py
│   │   └── valid_schemas.py
│   ├── settings.py
│   └── utils.py
├── logs
│   ├── ..
└── tests
    ├── conftest.py
    └── test_urls.py
```

#### 项目依赖
* Python3
* Flask==0.12.2
* voluptuous==0.9.3
* gevent>=1.3.1
* Flask-Script==2.0.5
* pytest==3.0.5
* gunicorn>=19.8.1
####使用

```
git clone git@git.oschina.net:zhinengtougu/flask-docker-scaffold.git product_name
cd product_name
rm -rf .git
git init
```

#### 运行命令

```
make run # 执行脚本
make test # 运行测试
```

#### 构建镜像与运行

```
make build # 创建flask镜像
docker run -p 5000:5000 -v "(your_log_path):/usr/src/app/logs" -id flask-docker-scaffold:beta # 运行容器

-------
# 或者
docker run -p 5000:5000 -v "(your_log_path):/usr/src/app/logs" -id r.p.cailve.cn/flask-docker-scaffold:basic
```


#### 访问
```
    http://localhost:4000/
```


