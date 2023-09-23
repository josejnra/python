export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"

npm install commitizen -g
commitizen init cz-conventional-changelog --save-dev --save-exact

npm install --save-dev @commitlint/cli
npm install --save-dev @commitlint/config-conventional
echo "module.exports = {extends: ['@commitlint/config-conventional']}" > commitlint.config.js


npm install husky --save-dev
npx husky install


if [ ! -f ".husky/prepare-commit-msg" ]
then
    npx husky add .husky/prepare-commit-msg "exec < /dev/tty && git cz --hook || true"
fi

if [ ! -f ".husky/commit-msg" ]
then
    npx husky add .husky/commit-msg 'npx --no -- commitlint --edit "$1"'
fi

sudo apt update -y
sudo apt-get install -y --reinstall xdg-utils

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
