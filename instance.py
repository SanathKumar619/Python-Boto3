import boto3

ec2=boto3.client('ec2')

a=ec2.describe_instances()

for i in a['Reservations']:
    for x in i['Instances']:
        term=ec2.terminate_instances(InstanceIds=x['InstanceId'])
