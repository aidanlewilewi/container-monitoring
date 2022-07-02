from prometheus_client import start_http_server, Counter
import docker
import json
import logging

STOP_EVENTS = ['die', 'kill', 'stop', 'exec_die', 'oom']
SOCKET = 'unix://var/run/docker.sock'

def log_events(client: docker.DockerClient, logger: logging):
    events = client.events()
    for event in events:
        json_event = json.loads(event)
        try:
            logging.info(json_event)
            print(json_event, '\n')
        except:
            pass 

if __name__ == '__main__':
    start_http_server(8000)

    logger = logging.basicConfig(filename='container_logging.log',
             encoding='utf-8',
             level=logging.DEBUG)

    log_events(docker.DockerClient(base_url=SOCKET), logger)
    
