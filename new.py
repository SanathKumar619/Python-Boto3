import boto3

groups=['Admin','he','new']

def list_users(usergroups):

    iam = boto3.client('iam')

    users=set()
    for i in usergroups:
        a=i
        paginator = iam.get_paginator('list_users')
        for i in paginator.paginate():
            b=iam.get_group(GroupName=a)
            c=b['Users']
            for i in c:
                users.add(i['UserName'])
    return users
user_list=list_users(groups)

print(user_list)
