import boto3

s3=boto3.client('s3')    #creating a s3 client

a=s3.list_buckets()      #creating alist bucket object

for i in a['Buckets']:
    b=s3.list_objects(Bucket=i['Name'])     #Creating list_object object
    for x in b['Contents']:
        response = s3.delete_objects(       #creating a delete_objects object / This object will delete all objects in a particular bucket
            Bucket=i['Name'],           
            Delete={
                'Objects': [{ 'Key' : x['Key'] } ],
                'Quiet': True
            }
        )
    print("All objects deleted")

    delete = s3.delete_bucket(Bucket=i['Name'])     #at last we are deleting Buckets
