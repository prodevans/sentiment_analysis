# FROM centos:7

# USER root
# #Downloading visual studio code server
# RUN yum install python3 wget -y

# EXPOSE 8080



# WORKDIR /app

# RUN yum group install "Development Tools" -y

# RUN yum install man-pages -y

# RUN gcc --version 

# # RUN python -m pip install --upgrade pip
FROM docker.io/ajay2307/ml-template:v1

COPY . /app

RUN pip3 install -r /app/requirements.txt

# RUN pip3 install --upgrade google-api-python-client 

CMD ["python3", "/app/analysis.py"]