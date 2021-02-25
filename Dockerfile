FROM python:3.7.2
ENV PYTHONIOENCODING utf-8

COPY . /code/

WORKDIR /code/

CMD ["python", "-u", "/code/hello_world.py"]
