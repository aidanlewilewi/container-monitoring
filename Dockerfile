FROM alpine:latest
WORKDIR .

RUN apk add --no-cache docker
#COPY events.sh .
#RUN chmod +x events.sh && ./events.sh
CMD ["docker", "events", "--format", "{{json .}}"]
