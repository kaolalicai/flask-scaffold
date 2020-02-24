from registry.cn-shenzhen.aliyuncs.com/xed/flask-docker-scaffold-ubuntu-base:latest

WORKDIR /usr/src/app
COPY requirements.txt ./
ENV PYTHONIOENCODING="utf-8"

# RUN pip3 install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple cython
RUN pip3 install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple numpy
RUN pip3 install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
