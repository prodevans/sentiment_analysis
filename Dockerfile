FROM python

USER root

EXPOSE 8080

COPY . /app

WORKDIR /app

RUN yum group install "Development Tools"

RUN yum install man-pages

RUN gcc --version 

RUN python -m pip install --upgrade pip

RUN pip install -r /app/requirements.txt

RUN pip install --upgrade google-api-python-client 

CMD ["python", "/app/analysis.py"]