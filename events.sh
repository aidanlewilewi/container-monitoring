#!/bin/sh
#docker events --format "{{json .}}" \
#       --filter event=stop \
#       --filter event=kill \
#       --filter event=die \
#       --filter event=oom      
python prometheus.py
