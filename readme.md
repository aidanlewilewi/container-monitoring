## Running:

docker build -t monitoring:latest . 
docker run --rm -v "/var/run/docker.sock:/var/run/docker.sock" -p 8000:8000 monitoring:latest


## Testing OOM
docker run -it -m 200M --memory-swap=300M progrium/stress --vm 1 --vm-bytes 500M

