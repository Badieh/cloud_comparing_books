#base image
FROM python:3.8-slim-buster
COPY . /Test
WORKDIR /Test
RUN pip install numpy
RUN pip install pandas
CMD python 'Cloud Assigment.py'