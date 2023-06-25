import boto3

iam_client = boto3.client('iam')

unique_user_names = set()

response = iam_client.list_groups()
groups = response['Groups']

for group in groups:
    group_name = group['GroupName']
    print(f"Group Name: {group_name}")

    response = iam_client.get_group(GroupName=group_name)
    users = response['Users']

    for user in users:
        user_name = user['UserName']
        print(f"User Name: {user_name}")

        unique_user_names.add(user_name)

for user_name in unique_user_name:
    response = iam_client.list_access_keys(UserName=user_name)
    access_keys = response['AccessKeyMetadata']

    for access_key in access_keys:
        access_key_id = access_key['AccessKeyId']
        print(f"Access Key ID: {access_key_id}")

        iam_client.update_access_key(
                UserName=user_name,
                AccessKeyId=access_key_id,
                Status='Inactive'
            )
        print(f"Deactivated access key {access_key_id} for user {user_name}")

        response = iam_client.create_access_key(UserName=user_name)
        new_access_key_id = response['AccessKey']['AccessKeyId']
        new_secret_access_key = response['AccessKey']['SecretAccessKey']
        print(f"Created new access key {new_access_key_id} for user {user_name}")

        iam_client.delete_access_key(UserName=user_name, AccessKeyId=access_key_id)
        print(f"Deleted old access key {access_key_id} for user {user_name}")


