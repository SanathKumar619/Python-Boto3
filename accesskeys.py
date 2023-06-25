import boto3
import pprint

# Create IAM client
iam = boto3.resource('iam')
a=[]
for i in iam.users.all():
    a.append(i)
print(a)
# List access keys through the pagination interface.
#paginator = iam.get_paginator('list_access_keys')
#for response in paginator.paginate(UserName='Sanath'):
  # pprint.pprint(response)
