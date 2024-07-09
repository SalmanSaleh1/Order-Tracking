FROM python:3.9
MAINTAINER Salman Alkhalifah

RUN apt-get update -y && apt-get install -y python3-pip python3-dev build-essential

COPY requiremnts.txt /app/requiremnts.txt
RUN pip install -r /app/requiremnts.txt

COPY src/ /root/src/
WORKDIR /root/src/

CMD ["python","flask_website/app.py"]