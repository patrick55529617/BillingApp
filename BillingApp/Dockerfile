FROM python:3.7.4
ENV PYTHONUNBUFFERED 1
LABEL maintainer patrick
RUN mkdir /BillingApp
WORKDIR /BillingApp
COPY . /BillingApp/
RUN pip3 install -r requirements.txt
