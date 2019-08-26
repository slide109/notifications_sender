FROM python:3.6-alpine

# Initialize
COPY ./requirements.txt /app/
WORKDIR /app

# Setup
RUN apk update
RUN apk upgrade
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# CMD flask run --host='0.0.0.0' --port=4040
CMD ["python", "src/run.py"]