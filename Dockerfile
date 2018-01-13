FROM python:3-alpine
WORKDIR /usr/src/app
ENV  TIME_ZONE Asia/Shanghai
RUN echo http://mirrors.aliyun.com/alpine/v3.4/main/ > /etc/apk/repositories && \
	echo http://mirrors.aliyun.com/alpine/v3.4/community/ >> /etc/apk/repositories && \
	echo http://mirrors.aliyun.com/alpine/edge/community/ >> /etc/apk/repositories && \
	apk update && \
    apk add --no-cache --virtual build-dependencies curl git subversion && \
    apk add --no-cache gcc g++ libgcc libstdc++ lapack-dev gfortran tzdata && \
    ln -sf /usr/share/zoneinfo/${TIME_ZONE} /etc/localtime && \
    echo "${TIME_ZONE}" > /etc/timezone
COPY requirements.txt ./
RUN pip install --no-cache-dir --verbose -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
RUN apk del build-dependencies
COPY . .
CMD ["python", "manage.py", "runserver", "-h", "0.0.0.0"]