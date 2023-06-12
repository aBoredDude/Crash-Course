FROM python:latest

ADD crash-course.py .

RUN pip install pandas lxml

CMD python3 ./crash-course.py