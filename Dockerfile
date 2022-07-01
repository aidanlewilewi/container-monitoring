FROM python:latest
WORKDIR .

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-u", "prometheus.py"]

#RUN apk add --no-cache docker
#COPY events.sh .
#RUN chmod +x events.sh && ./events.sh
#CMD ["docker", "events", "--format", "{{json .}}"]
#ADD events.sh .
#RUN chmod +x events.sh
#CMD ["./events.sh"]



