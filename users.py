import boto3
import pprint

resource=boto3.resource("iam")

#pprint.pprint(dir(resource))

for i in resource.users.all():
    print(i)
