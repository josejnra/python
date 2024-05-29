# My collection of learnings, notes and snippets on Python

This repository contains a collection of snippets on Python.

## Python
Python is an object oriented dynamically typed programming language
When you run a Python program, the interpreter first compiles it to bytecode and then runs the bytecode. So you could say that Python is compiled.
Python is technically not compiled nor interpreted, because Python is a language and you can write an interpreter or a compiler for any language.Still, most languages are considered either "compiled" or "interpreted" because they are most commonly implemented with a compiler or interpreter. In this sense, C++ is compiled and Python is interpreted.

The Python interpreter software downloaded from python.org is called **CPython** because it's written in C.

### CPython
CPython is the implementation of the language called “Python” in C. Python is an interpreted programming language. Hence, Python programmers need interpreters to convert Python code into machine code. Whereas **Cython** is a compiled programming language. The **Cython** programs can be executed directly by the CPU of the underlying computer without using any interpreter. There are other Implementations are like **Jython**, **Pypy**, **Ironpython** depending upon the language platform.

### Cython
Cython is designed as a C-extension for Python. The developers can use Cython to speed up Python code execution. But they can still write and run Python programs without using Cython. But the programmers have to install both Python and C-compiler as a pre-requisite to run Cython programs.

### Jython

Jython is an implementation of the Python language for the Java platform. Jython 2.7 implements the same language as CPython 2.7, and nearly all of the Core Python standard library modules. (CPython is the C implementation of the Python language.)
Writing Jython is similar to writing standard Python. The main difference is that since it compiles to Java Bytecode you can smoothly interact with Java Libraries. Of course it has a requirement on the JVM but has no Global Interpreter Lock (Famous GIL).

## poetry
In order to export requirements.txt, just run:
```shell
poetry export --without-hashes -o requirements.txt
```

## aws-vault
[AWS Vault](https://99designs.com/blog/engineering/aws-vault/) is a tool to securely store and access AWS credentials in a development environment.

First off, have `.aws/config` configured based on the profiles to be used. Then:

```shell
# List profiles
aws-vault list

# Set access key and secret key for the "main" profile
aws-vault add <profile-name>

# if you're using a container to run aws commands skip this.
# if you have aws-cli installed: get temporary credentials for a profile, defaults to admin.
/workspaces/python/.devcontainer/aws_temp_crendentials.sh <optional-profile-name>

# Assume role
aws-vault exec admin --duration=1h

# Rotate Access Key and Secret Access Key for the user
aws-vault rotate default
```

## awscli

This project uses the Docker image `amazon/aws-cli` for running aws cli commands. For that purpose a linux _alias_ was defined in [](.devcontainer/setup.sh). After we may simply run:

```shell
aws iam list-roles
```

```shell
aws sts get-caller-identity
```

```shell
aws sts assume-role --role-arn arn:aws:iam::<account-id>:role/<role-name> --role-session-name my-role-session
```

## When to use python
Python is a general-purpose language, which means it’s designed to be used in a range of applications, including data science, software and web development, automation, and generally getting stuff done. Python is commonly used for developing websites and software, task automation, data analysis, and data visualization. Since it’s relatively easy to learn, Python has been adopted by many non-programmers such as accountants and scientists, for a variety of everyday tasks, like organizing finances.


## Referencies
- https://www.coursera.org/articles/what-is-python-used-for-a-beginners-guide-to-using-python
- [aws-vault](https://github.com/99designs/aws-vault)
- [AWS CLI v2 doc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html)
