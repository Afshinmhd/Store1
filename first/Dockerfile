FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -U pip

RUN pip install -r requirements.txt 

COPY . /code/

EXPOSE 8000

CMD ["gunicorn","first.wsgi",":8000"]
