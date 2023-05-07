# syntax=docker/dockerfile:1
FROM python:3.10.6

# ensures python output is sent straight to terminal
ENV PYTHONUNBUFFERED 1

# prevents Python from copying pyc files to the container
ENV PYTHONDONTWRITEBYTECODE 1

# set the working directory in the container
RUN mkdir /code
WORKDIR /code/

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# copy the content of the local directory to the working directory
COPY . .
