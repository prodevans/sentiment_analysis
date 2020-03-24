FROM python

EXPOSE 8080

COPY . /app

WORKDIR /app

RUN python -m pip install --upgrade pip

RUN pip install -r /app/requirements.txt

RUN pip install --upgrade google-api-python-client 

CMD ["python", "/app/analysis.py"]