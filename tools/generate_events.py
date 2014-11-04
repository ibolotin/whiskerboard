#!/bin/env python
import sys
from api import WhiskerBoardApi

status = WhiskerBoardApi(user=sys.argv[1], password=sys.argv[2])

SERVICES = ['fx-hello', 'fx-sync', 'fxa']
MAX = 1


for service in SERVICES:
    count = 0
    while count < MAX:
        status.update_status('warning', 'Issue: %s is degraded.'.format(
            service), service)
        status.update_status('down', 'Issue: %s is down.'.format(
            service), service)
        status.update_status('up', 'Resolved: %s is operational.'.format(
            service), service)
        count += 1
