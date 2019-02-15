FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN pip install django
ADD . /code/
WORKDIR /code/docker_py
RUN python manage.py makemigrations && python manage.py migrate
# Server
EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

#docker build -t bonus_py .
#docker run -it --rm -p 8000:8000 bonus_py
