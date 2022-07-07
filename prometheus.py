from prometheus_client import start_http_server, Counter, Gauge, Info, Enum
import docker
import json
import logging
import sys

EVENTS = ['start', 'exec_start', 'create', 'pause', 'unpause' 'die', 'kill', 'stop', 'exec_die', 'oom']
SOCKET = 'unix://var/run/docker.sock'
PORT = 8000


def build_logs(event):
    """ Builds a dictionary of useful information about Docker events"""
    try:
        if event['status'] in EVENTS:
            # can do some filtering of the JSON here if we want
            return event
    except(KeyError):
        pass

def format_inspect(inspection):
    """ Formats the output of the Docker Inspect command"""
    pass

def main():
    client = docker.DockerClient(base_url=SOCKET)

    logging.basicConfig(encoding='utf-8',
                                level=logging.DEBUG,
                                filename='events.log',
                                #stream=sys.stdout,
                                format='%(message)s\n')
    event_logger = logging.getLogger()
    
    start_http_server(PORT)
    all_containers = []

    for event in client.events(decode=True):

        event_info = build_logs(event)
        if event_info is not None:
            event_logger.debug(event_info)
            
        # do something else with the info here?

        try:
            # get the Docker inspect information about the dead container. Only do it once per container
            if event['id'] not in all_containers: 
                all_containers.append(event['id'])
                inspect = format_inspect(client.api.inspect_container(event['id']))
        except(KeyError):
            pass



if __name__ == '__main__':
    main()
