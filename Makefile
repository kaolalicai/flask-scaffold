NAME=flask-docker-scaffold
TAG=beta

test:
	py.test tests -s

build:
	docker build --no-cache -t ${NAME}:${TAG} .
