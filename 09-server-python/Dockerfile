FROM ubuntu:18.04
LABEL author="Tomás"

# Set environment
ARG ENVIRONMENT
ENV SERVICE_ENVIRONMENT ${ENVIRONMENT}

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

# Supervisord folders
RUN mkdir -p /var/log/supervisor/; \
    touch /tmp/supervisor.sock


# nginx files
RUN mkdir -p /run/nginx/; \
    touch /run/nginx/nginx.pid


RUN apt-get update
RUN apt-get install -y python3.8 \
    nginx \
    gunicorn

RUN apt -y install python3-pip
RUN pip3 install supervisor

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

RUN python --version & pip --version

RUN mkdir -p ${APP_HOME}
WORKDIR ${APP_HOME}
ADD requirements.txt ${APP_HOME}
RUN pwd & ls
RUN apt-get -y install libpq-dev python3-dev
RUN pip install -r requirements.txt
ADD . ${APP_HOME}

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY run.sh ${APP_HOME}/run.sh
COPY supervisord.conf ${APP_HOME}/supervisord.conf

ENTRYPOINT [ "supervisord", "-n", "-c", "/home/app/web/supervisord.conf" ]