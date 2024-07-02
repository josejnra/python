#!/bin/bash

sudo apt update -y
sudo apt-get install -y --reinstall xdg-utils graphviz

npm install

poetry install
poetry update

# install aws-vault
# https://github.com/99designs/aws-vault/releases
sudo curl -L -o /usr/local/bin/aws-vault https://github.com/99designs/aws-vault/releases/download/v7.2.0/aws-vault-linux-amd64
sudo chmod 755 /usr/local/bin/aws-vault

# set backend being file, the other options are not working on devcontainer
echo "export AWS_VAULT_BACKEND=file" >> ~/.bashrc
# in order to run aws commands
echo "alias aws='docker run --rm -it -v ~/.aws:/root/.aws -v $(pwd):/aws amazon/aws-cli'" >> ~/.bashrc

git config --local core.editor "vi"
