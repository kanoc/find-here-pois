FROM python:3.7-slim
MAINTAINER Csaba Szotyori <kanocspam@gmail.com>

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/app
COPY tasks.py setup.py requirements.in requirements.txt /opt/services/app/
COPY api /opt/services/app/api/

WORKDIR /opt/services/app/
RUN pip install -r requirements.txt && inv install

EXPOSE 9000

CMD ["python", "/opt/services/app/api/web/server.py"]
