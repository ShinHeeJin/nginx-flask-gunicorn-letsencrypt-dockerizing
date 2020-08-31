FROM openjdk:8-jdk
COPY --from=python:3.6.8 / /

ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir -p /home/project/mr_backend
WORKDIR /home/project/mr_backend
COPY requirements.txt /home/project/mr_backend
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/mr_backend