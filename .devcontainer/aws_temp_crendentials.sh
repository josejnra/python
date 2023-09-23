#!/bin/bash

PROFILE="${VARIABLE:-admin}"

# export credentials and save it in credentials file
aws-vault export $PROFILE > ~/.aws/credentials
echo "$(echo '[default]'; cat ~/.aws/credentials)" > ~/.aws/credentials
echo "AWS_PAGER=" >> ~/.aws/credentials
echo "cli_pager=" >> ~/.aws/credentials
