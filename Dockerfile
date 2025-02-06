FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteraactive

RUN apt update && apt install -y \
	python3 \
	arduino \
	python3-pip && \
	mkdir -p /app/logs

RUN pip3 install pyserial

COPY . /app
WORKDIR /app

CMD ["python3", "test.py"]
