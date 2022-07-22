#! /usr/bin/env python

import os
import sys
import yaml

with open('task.yaml', 'r') as ymlfile:
    config = yaml.load(ymlfile,Loader=yaml.SafeLoader)

for task in config['tasks']:

    print('Task Name  : ', task.get('name:', 'None'))
    print('Description: ', task.get('description', 'None'))
    print('Status     : ', task.get('status:', 0))

    status = task.get('status', 0)
    if status < 0:
        sys.exit(status)

sys.exit(0)
