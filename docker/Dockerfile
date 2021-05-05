# using ubuntu 20.04 as a base
FROM ubuntu:20.04

RUN apt-get -y update
RUN apt-get -y upgrade

RUN apt-get install -y curl

# installation python3.8 and pip3.8
RUN apt-get install -y python3.8 python3.8-distutils
RUN curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py
RUN python3.8 /tmp/get-pip.py

# installation requirement library using requirement.txt
ADD requirements.txt /tmp/
RUN pip3.8 install -r /tmp/requirements.txt
