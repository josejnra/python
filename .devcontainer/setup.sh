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

npm install
npm run generate-requirements
npm run thaw
