import boto3
import json
import random
import time
from datetime import datetime, timedelta

cloudwatch = boto3.client('logs')

LOG_GROUP = '/dora/metrics'
LOG_STREAM = 'deployments'

# Ensure log group/stream exist
def setup_logs():
    try:
        cloudwatch.create_log_group(logGroupName=LOG_GROUP)
    except cloudwatch.exceptions.ResourceAlreadyExistsException:
        pass

    try:
        cloudwatch.create_log_stream(logGroupName=LOG_GROUP, logStreamName=LOG_STREAM)
    except cloudwatch.exceptions.ResourceAlreadyExistsException:
        pass

def push_events():
    devs = ['alice', 'bob', 'carol', 'dan']
    services = ['checkout', 'billing', 'recommendation']
    outcomes = ['success', 'failure']
    
    events = []
    timestamp = int(time.time() * 1000)
    
    for i in range(10):
        event = {
            'developer': random.choice(devs),
            'service': random.choice(services),
            'timestamp': datetime.now().isoformat(),
            'duration_sec': random.randint(30, 300),
            'event_type': random.choice(['deployment', 'recovery']),
            'outcome': random.choice(outcomes),
        }

        log_event = {
            'timestamp': timestamp + i * 1000,
            'message': json.dumps(event)
        }
        events.append(log_event)

    # Send logs
    response = cloudwatch.put_log_events(
        logGroupName=LOG_GROUP,
        logStreamName=LOG_STREAM,
        logEvents=events
    )
    print("Events pushed.")

setup_logs()
push_events()
