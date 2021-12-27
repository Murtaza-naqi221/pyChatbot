FROM python:3.7-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN python -m nltk.downloader punkt

COPY . .

RUN python train.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]