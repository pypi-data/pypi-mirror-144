# cfn-exec

This is Wrapper tool for aws cloudformation create stack.

## Installation

1. Open AWS Cloudshell or any terminal configured with aws cli.
2. Install cfn-exec
```sh
pip3 install cfnexec
```
3. Create stack with CFn file or url and parameter file or url
```sh
cfn-exec -n $your_stack_name -i $your_cfn_url -p $your_cfn_parameter_url 
```
note: If you are using the nested call function of Cloudformation, you need to make the called file accessible in advance.

### cli options

```sh
usage: cfn-exec [-h] [-i INPUT_PATH] [-n STACK_NAME] [-p PARAM]
                [--role-arn ROLE_ARN] [-s3 S3_BUCKET_URL_PARAMETER_KEY_NAME]
                [-csf] [-dr] [-del] [-v] [-V]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_PATH, --input-path INPUT_PATH
                        Cloudformation file url path having Cloudformation
                        files. Supported yaml and json. If this path is a
                        folder, it will be detected recursively.
  -n STACK_NAME, --stack-name STACK_NAME
                        The name that's associated with the stack. The name
                        must be unique in the Region in which you are creating
                        the stack.
  -p PARAM, --parameter-file PARAM
                        Parameter file
  --role-arn ROLE_ARN   The Amazon Resource Name (ARN) of an Identity and
                        Access Management (IAM) role that CloudFormation
                        assumes to create the stack. CloudFormation uses the
                        role's credentials to make calls on your behalf.
                        CloudFormation always uses this role for all future
                        operations on the stack. Provided that users have
                        permission to operate on the stack, CloudFormation
                        uses this role even if the users don't have permission
                        to pass it. Ensure that the role grants least
                        privilege. If you don't specify a value,
                        CloudFormation uses the role that was previously
                        associated with the stack. If no role is available,
                        CloudFormation uses a temporary session that's
                        generated from your user credentials.
  -s3 S3_BUCKET_URL_PARAMETER_KEY_NAME, --s3-bucket-url-parameter-key-name S3_BUCKET_URL_PARAMETER_KEY_NAME
                        Set the parameter key name to this, if the input path
                        is a local file and you want to reflect the S3 bucket
                        name to be uploaded in the parameter.
  -csf, --change-set-force-deploy
                        When the target Stack already exists and is to be
                        deployed as a change set, enabling this option will
                        apply the change set to the stack as is.
  -dr, --disable-roleback
                        Disable rollback on stack creation failure.
  -del, --delete-stack  After creating a stack, the stack is deleted
                        regardless of success or failure.
  -v, --version         Show version information and quit.
  -V, --verbose         give more detailed output
```

### parameter file format

Support "Cloudformation official format" or "Simple format"
**Cloudformation official format**
```json
[
  {
    "ParameterKey": "ParameterKeyName1",
    "ParameterValue": "ParameterValue1"
  },
  {
    "ParameterKey": "ParameterKeyName2",
    "ParameterValue": "ParameterValue2"
  },
  ...
],
```
```yaml
---
- ParameterKey: ParameterKeyName1
  ParameterValue: ParameterValue1
- ParameterKey: ParameterKeyName2
  ParameterValue: ParameterValue2
  ...
```
**Simple format**
```json
{
  "ParameterKeyName1": "ParameterValue1",
  "ParameterKeyName2": "ParameterValue2",
  ...
}
```
```yaml
---
ParameterKeyName1: ParameterValue1
ParameterKeyName2: ParameterValue2
...
```

### Nested Template

If the --input-path Cloudformation template has a nested structure that references another template, note the following
* If --input-path is set by URL, all referenced templates must have been placed at the referenced URL in advance.
* If --input-path is set as a local file, the referenced template must be located under the folder where the target local file is located. Also, the referenced URL must be able to be changed via parameters.

#### Reference to local files with nested structure

This is a reference example of a Cloudformation file with a nested structure set by --input-path.
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: main.yml
Parameters: 
  TemplateS3BucketURL:
    Description: Referenced S3 bucket URL
    Type: String
    Default: TemplateS3BucketURL
  BucketName:
    Type: String
    Default: BucketName

Resources:
  # Create S3 Bucket
  S3:
    Type: AWS::CloudFormation::Stack
    Properties:
      TemplateURL: !Sub ${TemplateS3BucketURL}/components/s3.yml
      Parameters:
        BucketName: !Ref BucketName
```

This is a reference example of a Cloudformation file with a nested structure set by --input-path.
```yaml
AWSTemplateFormatVersion: "2010-09-09"
Description: s3.yml
Parameters:
  BucketName:
    Type: String
    Default: "BucketName"

Resources:
  S3Bucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Ref BucketName
```

This is an example of a parameter file.
```yaml
TemplateS3BucketURL: TemplateS3BucketURL
BucketName: cfnexec-example-test-01234567890123456789
```

This is the folder tree of the local file.
```
.
└── example
    ├── param.yml
    └── input
        ├── main.yml
        └── components
            └── s3.yml
```

This is an example of execution.
```sh
cfn-exec -n example-stack -i ./example/input/main.yml -p ./example/param.yml -s3 TemplateS3BucketURL
```

## Usage

Supported Cloudformation and parameter files are written in json or yaml format, and can be located at local, S3, or public URLs.

### local file
```sh
cfn-exec -n example-stack -i ./example/input/main.yml -p ./example/param.yml
```

### s3 file
```sh
cfn-exec -n example-stack -i https://yourbucket.s3.us-east-1.amazonaws.com/main.yml -p https://yourbucket.s3.us-east-1.amazonaws.com/param.yml
```

### public file
```sh
cfn-exec -n example-stack -i https://raw.githubusercontent.com/youraccount/yourrepo/main/input/main.yml -p https://raw.githubusercontent.com/youraccount/yourrepo/main/param.yml
```
