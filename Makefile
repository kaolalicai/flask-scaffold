NAMESPACE=xed
NAME=flask-docker-scaffold

# if not need name space open line 5 and add comment the line 6
# FIXED_NAME=${NAME}
FIXED_NAME=${NAMESPACE}/${NAME}

# base package/test package send to sz. prod send to ind 
SZ_REGISTRY=registry.cn-shenzhen.aliyuncs.com
IND_REGISTRY=registry.ap-south-1.aliyuncs.com

run:
	export ENVIRONMENT=default; gunicorn manage:app -c ./gunicorn_helper.py

tests:
	py.test test -s

build-ubuntu:
	cp ./docker/ubuntu_base/Dockerfile ./
	docker build -t ${SZ_REGISTRY}/${FIXED_NAME}-ubuntu-base:latest .
	docker tag ${SZ_REGISTRY}/${FIXED_NAME}-ubuntu-base:pre-latest ${SZ_REGISTRY}/${FIXED_NAME}-ubuntu-base:latest
	docker push ${SZ_REGISTRY}/${FIXED_NAME}-ubuntu-base:latest
	rm ./Dockerfile

build-base:
	cp ./docker/base/Dockerfile ./
	docker build -t ${SZ_REGISTRY}/${NAMESPACE}/${NAME}-base:latest .
	docker tag ${SZ_REGISTRY}/${FIXED_NAME}-base:pre-latest ${SZ_REGISTRY}/${FIXED_NAME}-base:latest
	docker push ${SZ_REGISTRY}/${NAMESPACE}/${NAME}-base:latest
	rm ./Dockerfile

build:
	cp ./docker/product/Dockerfile ./
	docker build --no-cache -t ${IND_REGISTRY}/${FIXED_NAME}:${TAG} .
	docker tag ${IND_REGISTRY}/${FIXED_NAME}:pre-${TAG} ${IND_REGISTRY}/${FIXED_NAME}:${TAG}
	docker push ${IND_REGISTRY}/${FIXED_NAME}:${TAG}
	rm ./Dockerfile

build-test:
	cp ./docker/product/Dockerfile ./
	docker build --no-cache -t ${SZ_REGISTRY}/${NAMESPACE}/${NAME}:${TAG} .
	docker tag ${SZ_REGISTRY}/${FIXED_NAME}:pre-${TAG} ${SZ_REGISTRY}/${FIXED_NAME}:${TAG}
	docker push ${SZ_REGISTRY}/${NAMESPACE}/${NAME}:${TAG}
	rm ./Dockerfile
	