############################################################
# Dockerfile to build swagger container images
# Based on Ubuntu
############################################################
FROM registry.opensource.zalan.do/stups/python:3.5.2-37

MAINTAINER Akash Rajguru

#Copy requred fils
COPY app.py $APP

# Update the repository sources list
RUN apt-get update

#Check if pip is available
RUN pip -V

#Install virtualevn
RUN pip install virtualenv &&\ 
		virtualenv myvirtualenv &&\
			cd myvirtualenv &&\ 
			/bin/bash -c "source ./bin/activate"

#Installing dependencies in virtualenv
RUN pip install connexion

#Creating project folder 
RUN mkdir empassetmage &&\ 
	cd empassetmage &&\
	mkdir swagger

CMD python app.py

