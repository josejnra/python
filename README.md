# My collection of learnings, notes and snippets on Python

This repository contains a collection of snippets on Python.

## poetry
In order to export requirements.txt, just run:
```shell
poetry export --without-hashes -o requirements.txt
```

## aws-vault
AWS Vault is a tool to securely store and access AWS credentials in a development environment.

```shell
# First access requires passing a access key and secret key
aws-vault add default

# List profiles
aws-vault list

# Assume role
aws-vault exec admin --duration=1h

# get temporary credentials for a profile, defautls to admin
/workspaces/python/.devcontainer/aws_temp_crendentials.sh <optional-profile-name>

# Rotate Access Key and Secret Access Key for the user
aws-vault rotate default
```

## awscli

This project uses the Docker image `amazon/aws-cli` for running aws cli commands. For that purpose a linux _alias_ was defined in [](.devcontainer/setup.sh). After we may simply run:

```shell
aws iam list-roles
```

## When to use python
Python is a general-purpose language, which means it’s designed to be used in a range of applications, including data science, software and web development, automation, and generally getting stuff done. Python is commonly used for developing websites and software, task automation, data analysis, and data visualization. Since it’s relatively easy to learn, Python has been adopted by many non-programmers such as accountants and scientists, for a variety of everyday tasks, like organizing finances.


## Referencies
- https://www.coursera.org/articles/what-is-python-used-for-a-beginners-guide-to-using-python
- [aws-vault](https://github.com/99designs/aws-vault)
- [AWS CLI v2 doc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html)
