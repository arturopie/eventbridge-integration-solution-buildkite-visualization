import json
from datetime import datetime
import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    uuid = event['detail']['job']['uuid']
    
    start_time = datetime.strptime((event['detail']['job']['started_at'])[:-4], '%Y-%m-%d %H:%M:%S')
    runnable_time = datetime.strptime((event['detail']['job']['runnable_at'])[:-4], '%Y-%m-%d %H:%M:%S')
    finish_time = datetime.strptime((event['detail']['job']['finished_at'])[:-4], '%Y-%m-%d %H:%M:%S')
    wait_time = start_time - runnable_time
    
    
    pipeline = event['detail']['pipeline']['slug']
    org = event['detail']['organization']['slug']
    
    print('Pipeline: {}, Org: {}, Job started after waiting {} seconds'.format(pipeline, org, wait_time))
    
    output =  json.dumps({
        "detail-type": "job-finished",
        "pipeline": pipeline,
        "org": org,
        "start_time" : start_time.isoformat(),
        "runnable_time": runnable_time.isoformat(),
        "finish_time": finish_time.isoformat()
    })
    
    print(output)
    
    response = s3.put_object(
        Body=output,
        Bucket=os.environ['s3bucket'],
        Key='buildkite-job-{}'.format(uuid)
    )
    
    print(response)