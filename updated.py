import boto3

iam = boto3.client('iam')

users=set()
usergroups = ['Admin','he']
for i in usergroups:
    a=i
    paginator = iam.get_paginator('list_users')
    for i in paginator.paginate():
        b=iam.get_group(GroupName=a)
        c=b['Users']
        for i in c:
            users.add(i['UserName'])
print(users)

