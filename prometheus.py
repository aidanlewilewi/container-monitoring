from prometheus_client import start_http_server, Counter
import docker
import json

if __name__ == '__main__':

    stop_events = ['die', 'kill', 'stop', 'exec_die', 'oom']

    start_http_server(8000)

    client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    events = client.events()
    c = Counter('container_stops', 'Container Stops')

    for event in events:
        json_event = json.loads(event)
        try:
            if json_event['status'] in stop_events:
                print(json_event['status']) 
                c.inc()
        except:
            pass 
