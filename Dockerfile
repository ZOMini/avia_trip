FROM python:3.9.7-slim
WORKDIR /avia
COPY avia/ .
RUN pip install -r requirements.txt
CMD ["gunicorn", "avia.wsgi:application", "--bind", "0:8000" ] 
