FROM registry.yandex.net/ubuntu:trusty
MAINTAINER borislitv@yandex-team.ru

RUN apt-get update -qq
RUN apt-get install python-setuptools python python-pip -y --force-yes
RUN pip install https://github.com/cocaine/cocaine-framework-python/archive/master.zip

ADD ./echo.py /root/echo.py
RUN chmod +x /root/echo.py
