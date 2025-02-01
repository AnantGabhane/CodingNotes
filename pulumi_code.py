"""An AWS Python Pulumi program"""

import pulumi # type: ignore
from pulumi_aws import iam, s3 # type: ignore

# Get stack name
stack = pulumi.get_stack()

# Create an S3 bucket
rgb_spliting_user_upload_bucket = s3.BucketV2(f"rgb-spliting-user-upload-{stack}")

# Define the bucket lifecycle configuration
s3.BucketLifecycleConfigurationV2(
    f"rgb-spliting-user-upload-lifecycle-{stack}",
    bucket=rgb_spliting_user_upload_bucket.id,
    rules=[
        {"id": "delete-after-1-day", "status": "Enabled", "expiration": {"days": 1}}
    ],
)

# Create an IAM User
nextjs_app_iam_user = iam.User(f"nextjs-app-user-{stack}")

# Create an IAM Policy for the user to access the S3 bucket
rgb_spliting_user_upload_read_write_policy = iam.Policy(
    f"rgb-spliting-user-upload-read-write-{stack}",
    policy=rgb_spliting_user_upload_bucket.arn.apply(
        lambda arn: {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "s3:PutObject",
                        "s3:GetObject",
                    ],
                    "Resource": f"{arn}/*",
                }
            ],
        }
    ),
)

# Attach the policy to the IAM User
nextjs_app_policy_attachment = iam.UserPolicyAttachment(
    f"nextjs-app-user-policy-attachment-{stack}",
    user=nextjs_app_iam_user.name,
    policy_arn=rgb_spliting_user_upload_read_write_policy.arn,
)

# Create an access key for the IAM user
nextjs_app_iam_user_access_key = iam.AccessKey(
    f"nextjs-app-access-key-{stack}",
    user=nextjs_app_iam_user.name,
)

# Export important values
pulumi.export("rgb_spliting_user_upload_bucket", rgb_spliting_user_upload_bucket.id)
pulumi.export("nextjs_app_iam_user_access_key_id", nextjs_app_iam_user_access_key.id)
pulumi.export(
    "nextjs_app_iam_user_secret_access_key", nextjs_app_iam_user_access_key.secret
)
