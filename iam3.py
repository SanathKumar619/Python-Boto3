import boto3

# Create IAM client
iam_client = boto3.client('iam')

# List the IAM groups
response = iam_client.list_groups()
groups = response['Groups']

# Iterate through each group
for group in groups:
    group_name = group['GroupName']
    print(f"Group Name: {group_name}")

    # List the users in the group
    response = iam_client.get_group(GroupName=group_name)
    users = response['Users']

    # Iterate through each user in the group
    for user in users:
        user_name = user['UserName']
        print(f"User Name: {user_name}")

        # Rotate access keys for the user
        response = iam_client.list_access_keys(UserName=user_name)
        access_keys = response['AccessKeyMetadata']

        # Iterate through each access key
        for access_key in access_keys:
            access_key_id = access_key['AccessKeyId']
            print(f"Access Key ID: {access_key_id}")

            # Deactivate the access key
            iam_client.update_access_key(
                UserName=user_name,
                AccessKeyId=access_key_id,
                Status='Inactive'
            )
            print(f"Deactivated access key {access_key_id} for user {user_name}")

            # Create a new access key
            response = iam_client.create_access_key(UserName=user_name)
            new_access_key_id = response['AccessKey']['AccessKeyId']
            new_secret_access_key = response['AccessKey']['SecretAccessKey']
            print(f"Created new access key {new_access_key_id} for user {user_name}")

            # Optionally, you can store the new access key details securely for future use
            # Make sure to securely manage the access key details, such as storing them in a secure key management system.

            # Delete the old access key
            iam_client.delete_access_key(UserName=user_name, AccessKeyId=access_key_id)
            print(f"Deleted old access key {access_key_id} for user {user_name}")

        print()

