FROM python:3.9

COPY ./requirements.txt /webapp/requirements.txt 
WORKDIR /app

RUN pip install -r requirements.txt

COPY app/* /app

ENTRYPOINT [ "uvicorn" ]

CMD [ "--host", "0.0.0.0", "main:app" ]