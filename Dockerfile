FROM ubuntu
MAINTAINER Thiago Resende, thiago.gcresende@gmail.com

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    python2.7 \
    curl

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN /usr/bin/python2.7 get-pip.py
RUN pip install scikit-learn
RUN mv /usr/bin/python2.7 /usr/bin/python
WORKDIR /var/www