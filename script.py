import boto3

client = boto3.client('resourcegroupstaggingapi')
elb = boto3.client('elbv2')

response = client.get_resources(
    TagFilters=[
        {
            'Key': 'resource',
            'Values': ['TG']
        },
    ],
    ResourcesPerPage=12,
)

for i in range(len(response['ResourceTagMappingList'])):
    ARN=str(response['ResourceTagMappingList'][i]['ResourceARN'])
    targetHealth = elb.describe_target_health(
        TargetGroupArn=ARN,
    )
    for j in range(len(targetHealth['TargetHealthDescriptions'])):
        print('below is detail of one TG')
        print(targetHealth['TargetHealthDescriptions'][j])
