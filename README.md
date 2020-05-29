### Flask Scaffold
------
#### 目录结构

```

├── docker
│   ├── ubuntu
│   │   └── Dockerfile.py # Ubuntu & 安装python3
│   ├── base
│   │   └── Dockerfile.py # 安装ubuntu依赖包以及python安装包
│   └── product
│       └── Dockerfile.py # 部署项目代码
├── app
│   ├── __init__.py # 初始配置, 包括log, 中间件, 错误检查等 
│   ├── router.py
│   ├── controller.py 
│   ├── service.py 
│   └── connection.py # DB链接
├── log
│   └── ..
├── Makefile
├── manage.py
├── README.md
├── requirements.txt 项目依赖
├── .gitignore
├── .dockerignore
└── test
    ├── conftest.py 单元测试配置的依赖
    └── test_urls.py 单元测试Demo
```

#### 项目依赖
* Python3
* requirement.txt

#### 框架使用

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

#### 构建镜像与运行:
1. 新的ubuntu基础包(基本不需要, 除非Ubuntu镜像需要安装一些包) ```make build_ubuntu```
2. 新的带python包的基础包(尽量不要用, 只有安装python新包的时候, 需要执行这个) ```make build_base```
3. 创建业务镜像 ```make build TAG=develop```
4. 运行容器 ```docker run -p 5000:5000 -v "(your_log_path):/usr/src/app/logs" -id flask-docker-scaffold:beta```

#### 访问:
http://localhost:5000/
