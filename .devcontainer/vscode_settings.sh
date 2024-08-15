#!/bin/bash

get_directory_name() {
  local path="$1"

  # check whether the path exists and if it's a directory
  if [ ! -d "$path" ]; then
    echo "Error: '$path' is not a valid directory."
    exit 1
  fi

  # count number of folder in the path
  local folder_count=$(find "$path" -maxdepth 1 -type d | wc -l)

  # check whether exists only one folder (ignoring current dir)
  if [ "$folder_count" -eq 2 ]; then
    # returns the name of the single directory
    local folder_name=$(basename "$path"/*/)
    echo "$folder_name"
  else
    echo "Error: It was expected only one directory, but it was found $((folder_count - 1))."
    exit 1
  fi
}

PROJECT_NAME=$(get_directory_name "/workspaces")

# path to VS Code settings file (settings.json)
VSCODE_SETTINGS_FOLDER_PATH="/workspaces/${PROJECT_NAME}/.vscode"
VSCODE_SETTINGS_PATH="${VSCODE_SETTINGS_FOLDER_PATH}/settings.json"

# check whether the settings file exists, if not create it
if [[ ! -f "$VSCODE_SETTINGS_PATH" ]]; then
    echo "File settings.json not found in $VSCODE_SETTINGS_PATH."
    echo $VSCODE_SETTINGS_FOLDER_PATH
    mkdir -p $VSCODE_SETTINGS_FOLDER_PATH
    touch $VSCODE_SETTINGS_PATH
    echo '{' >> $VSCODE_SETTINGS_PATH
    echo '}' >> $VSCODE_SETTINGS_PATH
    echo "File ${VSCODE_SETTINGS_PATH} has been created"
fi

update_setting() {
    local key="$1"
    local value="$2"

    # removes quotes around the curly bracket to avoid replacement issues
    local key_stripped="${key//\"/}"

    # uses jq to check whether the key already exists in settings.json
    if jq -e ".\"$key_stripped\"" "$VSCODE_SETTINGS_PATH" > /dev/null; then
        # if exists, update value
        jq ".\"$key_stripped\" = $value" "$VSCODE_SETTINGS_PATH" > tmp.$$.json && mv tmp.$$.json "$VSCODE_SETTINGS_PATH"
        echo "A configuração \"$key\" foi atualizada."
    else
        # if doesn't exist, add config before last '}' in the file
        jq ". + {\"$key_stripped\": $value}" "$VSCODE_SETTINGS_PATH" > tmp.$$.json && mv tmp.$$.json "$VSCODE_SETTINGS_PATH"
        echo "A configuração \"$key\" foi adicionada."
    fi
}

venv_folder_name=$(get_directory_name "/home/vscode/.cache/pypoetry/virtualenvs")

# print directory's name (if found)
if [ -n "$venv_folder_name" ]; then
  echo "Venv found: $venv_folder_name"
fi

# set settings
update_setting "python.defaultInterpreterPath" '"/home/vscode/.cache/pypoetry/virtualenvs/'${venv_folder_name}'/bin/python"'
update_setting "mypy.dmypyExecutable" '"/home/vscode/.cache/pypoetry/virtualenvs/'${venv_folder_name}'/bin/dmypy"'
update_setting "mypy-type-checker.path" '["/home/vscode/.cache/pypoetry/virtualenvs/'${venv_folder_name}'/bin/mypy"]'
update_setting "python.testing.pytestPath" '"/home/vscode/.cache/pypoetry/virtualenvs/'${venv_folder_name}'/bin/pytest"'
update_setting "flake8.interpreter" '["/home/vscode/.cache/pypoetry/virtualenvs/'${venv_folder_name}'/bin/flake8"]'
update_setting "flake8.path" '["/home/vscode/.cache/pypoetry/virtualenvs/'${venv_folder_name}'/bin/flake8"]'

echo "VS Code settings has been updated."
