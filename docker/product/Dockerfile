from registry.cn-shenzhen.aliyuncs.com/xed/flask-docker-scaffold-base:latest
COPY . .
CMD ["gunicorn", "manage:app", "-c", "./gunicorn_helper.py"]