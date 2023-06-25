
from datetime import datetime,timezone
import boto3
import pprint

max_age = 90
iam=boto3.client('iam')
today=datetime.now(timezone.utc)

page=iam.get_paginator('list_users')

for i in page.paginate():
    for user in i['Users']:
        a=user['UserName']
        b=iam.list_access_keys(UserName=a)

        for c in b['AccessKeyMetadata']:
            access_key=c['AccessKeyId']
            key_creation_date=c['CreateDate']
            age=(today - key_creation_date).days
            print(access_key)

            if age>max_age:
                print(f"Deleting the access key for the user named {a}, Because access key is older than {max_age}")
                d = client.update_access_key(
                UserName=a,
                AccessKeyId=access_key,
                Status='Inactive'
                )
                
                iam.delete_access_key(Username=a,AccessKeyId=access_key)

                print(f"old acesskey has been deleted for user = $a")

                create=iam.create_access_key(UserName=a)
                new_access_key_id = create['AccessKey']['AccessKeyId']
                new_secret_access_key = create['AccessKey']['SecretAccessKey']
                print(f"Created new access key {new_access_key_id} for user {user_name}")

