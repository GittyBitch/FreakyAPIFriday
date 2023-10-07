#!/bin/bash
aws cloudformation create-stack --stack-name FreakyAPIFriday --template-body file://CodeBuild-CloudFormation.yaml --capabilities CAPABILITY_IAM

