FROM python:3.10

ENV DockerHome=/home/app/ampics

RUN mkdir -p $DockerHome

WORKDIR $DockerHome

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . $DockerHome

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver
