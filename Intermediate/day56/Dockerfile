FROM centos

RUN yum update -y
RUN yum install python3 -y
RUN pip-3.6 install flask

COPY webapps /opt/
ENTRYPOINT FLASK_APP=/opt/server.py flask run -h 0.0.0.0 -p 80