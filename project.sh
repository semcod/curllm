#!/usr/bin/env bash
set -e
clear

VENV="venv"
PIP="$VENV/bin/pip"

if [ ! -f "$PIP" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$VENV"
fi

$PIP install -e .
$PIP install regix --upgrade --quiet
#$PIP install pyqual --upgrade --quiet
$PIP install prefact --upgrade --quiet
$PIP install vallm --upgrade --quiet
$PIP install redup --upgrade --quiet
$PIP install glon --upgrade --quiet
$PIP install code2logic --upgrade --quiet
$PIP install code2llm --upgrade --quiet
#$VENV/bin/code2llm ./ -f toon,evolution,code2logic,project-yaml -o ./project --no-chunk
$VENV/bin/code2llm ./ -f all -o ./project --no-chunk --exclude '*.md'
#$VENV/bin/code2llm report --format all       # → all views

#$PIP install code2docs --upgrade --quiet
#$VENV/bin/code2docs ./ --readme-only
$VENV/bin/redup scan . --format toon --output ./project
#$VENV/bin/redup scan . --functions-only -f toon --output ./project
#$VENV/bin/vallm batch ./src --recursive --semantic --model qwen2.5-coder:7b
#$VENV/bin/vallm batch --parallel .
#$VENV/bin/vallm batch . --recursive --format toon --output ./project
$VENV/bin/prefact -a -e "examples/**"


$PIP install doql --upgrade --quiet
$VENV/bin/doql adopt . --format less --output app.doql.less --force

$PIP install sumd --upgrade --quiet
$VENV/bin/sumd .
$VENV/bin/sumr .


if [ -d "../goal/goal" ] && [ -f "../goal/pyproject.toml" ]; then
    pip install -e ../goal
    $PIP install -e ../goal --quiet
else
    pip install -U goal
    $PIP install goal --upgrade --quiet
fi
#$VENV/bin/goal -a

if [ -x "./tree.sh" ]; then
    bash ./tree.sh
elif command -v tree >/dev/null 2>&1; then
    tree -L 2
else
    echo "Skipping tree snapshot: ./tree.sh not found and 'tree' is not installed."
fi