import boto3

ami = boto3.client('ec2')

a=ami.describe_images(Owners=["self"])

for i in a["Images"]:
    img_id=i["ImageId"]
    
    b=ami.deregister_image(ImageId=img_id)
   
    print(f"Ami deleted is with ami-id: {img_id}")

c=ami.describe_snapshots(OwnerIds=["080627685068"])

for i in c["Snapshots"]:
    snap_id=i["SnapshotId"]
     
    d=ami.delete_snapshot(SnapshotId=snap_id)
    print(f"snap deleted is with id {snap_id}")

