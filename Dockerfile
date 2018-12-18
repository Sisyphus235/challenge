FROM python:alpine

ADD ./ /vol
WORKDIR /vol
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
EXPOSE 5003
ENTRYPOINT ["sh", "docker_entrypoint.sh"]