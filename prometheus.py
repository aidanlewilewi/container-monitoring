from prometheus_client import start_http_server, Counter
import docker
import json

stop_events = ['die', 'kill', 'stop', 'exec_die', 'oom']

def print_container_stops(client):
    events = client.events()
    for event in events:
        json_event = json.loads(event)
        try:
            if json_event['status'] in stop_events:
                print(json_event['status']) 
        except:
            pass 

if __name__ == '__main__':

    start_http_server(8000)

    print_container_stops(docker.DockerClient(base_url='unix://var/run/docker.sock'))
    
