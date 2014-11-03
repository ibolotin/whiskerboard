#!/bin/env python
import sys
from api import WhiskerBoardApi

status = WhiskerBoardApi(user=sys.argv[1], password=sys.argv[2])

SERVICES = ['fx-hello', 'fx-sync', 'fxa']


for service in SERVICES:
    count = 0
    while count < 3:
        status.update_status('warning', '%s are degraded' % service, service)
        status.update_status('down', '%s are down.' % service, service)
        status.update_status('up', '%s operational.' % service, service)
        count += 1
