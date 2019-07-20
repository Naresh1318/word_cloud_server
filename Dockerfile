FROM python:3.6

# Need to install uWSGI
RUN apt-get update
RUN apt-get install -y build-essential

ADD requirements.txt /tmp/requirements.txt
RUN pip install --trusted-host pypi.python.org -r /tmp/requirements.txt

WORKDIR /word_cloud_server
COPY . /word_cloud_server

EXPOSE 5000

CMD ["uwsgi", "--ini", "word_cloud_server.ini"]
