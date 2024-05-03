# Identity and Access Management (IAM)

## IAM Policy Document
```json
{
  "version": "2012-10-17",
  "Statement": [
    {
      "Sid": "FullAccess",
      "Effect": "Allow",
      "Action": ["s3:*"]
      "Resource": ["*"]
    },
    {
      "Sid": "DenyCatBucket",
      "Effect": "Deny",
      "Action": ["s3:*"]
      "Resource": ["arn:aws:s3:::catgifs", "arn:aws:s3:::catgifs/*"]
    }
  ]
}
```
- By default everything is deny
- Deny take priority over allow

## IAM Users
- IAM users are identity used for anything requiring long term AWS access eg. Human, Application, service accounts
- Principal = Human/Application/Group
- facts
  - 5000 IAM user per account
  - IAM user can be memeber of 10 groups

## Amazon Resource Name (ARN)
- Uniquely identify a resouce in AWS
- format
  - arn:partition:service:region:account:account-id:resource-id
  - arn:partition:service:region:account:account-id:resource-type/resource-id
  - arn:partition:service:region:account:account-id:resource-type:resource-id
- format eg.
  - arn:aws:s3:::catgif -> this refers to bucket only
  - arn:aws:s3:::catgif/*  -> this refers to all Objects in bucket but not bucket itself

## IAM Roles
- No of user assigned to a Role
- Role can be used as temp basis

## IAM Groups
- It is containers for IAM Users
- Groups are not true identity, they can't be referenced as principle in a policy















