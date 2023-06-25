import boto3
import pprint
instance=boto3.client('ec2')
ec2=instance.describe_instances()
pprint.pprint(dir(instance))

