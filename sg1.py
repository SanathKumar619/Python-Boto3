import boto3

li=list()
ec2=boto3.client('ec2')

a=ec2.describe_security_groups()

for i in a['SecurityGroups']:
    li.append(i['GroupName'])

for v in li:
    b=ec2.describe_instances()
    for x in b['Reservations']:
        for y in x['Instances']:
            for z in y['SecurityGroups']:
                sg=z['GroupName']
                if v=='default':
                    continue
                elif v==sg:
                    continue
                else:
                    de=ec2.delete_security_group(GroupName=v)

