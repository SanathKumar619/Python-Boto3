import boto3

iam = boto3.client('iam')
sns=boto3.client('sns')

z=sns.create_topic(Name='Sanath')
topic_arn=z['TopicArn']
y=sns.subscribe(TopicArn=topic_arn,Protocol='email',Endpoint='sanath_kumar1@thbs.com')
sub_arn=y['SubscriptionArn']

users=set()
a = iam.list_groups()
groups = a['Groups']

for i in groups:
    Group_names=i['GroupName']
    b=iam.get_group(GroupName=Group_names)
    c=b['Users']
    for i in c:
        users.add(i['UserName'])
print(f'Unique users are {users}')

for i in users:
    d=iam.list_access_keys(UserName=i)
    e=d['AccessKeyMetadata']
    for i in e:
        uname=i['UserName']
        access_id=i['AccessKeyId']
        f = iam.update_access_key(
            UserName=uname,
            AccessKeyId=access_id,
            Status='Inactive'
            )
        print(f'Access key has been deactivated for the user = {uname}')

        g= iam.delete_access_key(
            UserName=uname,
            AccessKeyId=access_id
            )
        print('Old access key has been deleted')

        h = iam.create_access_key(
            UserName=uname
            )
        new_access=h['AccessKey']['AccessKeyId']
        new_secret=h['AccessKey']['SecretAccessKey']
        c=sns.publish(TopicArn=topic_arn,Message=f'Here is the updated Access key = {new_access} and Secret_key={new_secret} for the user = {uname}')
