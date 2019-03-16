FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get update && apt-get install -y build-essential checkinstall \
 && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*
RUN wget -np -O Python-2.7.13.tar.xz https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tar.xz && \
    tar -xvf Python-2.7.13.tar.xz && \
    cd Python-2.7.13 && \
    ./configure --prefix=/usr/local && \
    make && \
    make altinstall && \
    cd - && \
    rm -rf Python-2.7.13*
WORKDIR /home/gangapr
COPY . .
RUN yes | cp -rf /home/gangapr/sources.list /etc/apt/sources.list 
RUN apt-get update
RUN apt-get install -y python-pip python-dev build-essential && pip install --upgrade pip 
RUN pip install -r requirements.txt
RUN yes | ganga -g
CMD ganga -i rjob.py