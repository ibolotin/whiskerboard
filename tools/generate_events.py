#!/bin/env python
import sys
from api import WhiskerBoardApi

status = WhiskerBoardApi(user=sys.argv[1], password=sys.argv[2])

SERVICES = ['fx-hello', 'fx-sync', 'fxa']
MAX = 1


for service in SERVICES:
    count = 0
    while count < MAX:
        status.update_status('warning', '%s is degraded.' % service, service)
        status.update_status('down', '%s is down.' % service, service)
        status.update_status('up', '%s operational.' % service, service)
        count += 1
