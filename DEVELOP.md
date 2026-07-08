# Sandbox guidelines

## Install

```shell
git clone https://github.com/pyveci/verlib2.git
cd verlib2
uv venv --python 3.14 --seed .venv
source .venv/bin/activate
uv pip install --upgrade --editable='.[develop,test,release]'
```

## Validate

Invoke linters and software tests.

```shell
poe check
```

## EOL Python

Use Docker to validate the package on EOL Python versions.

```shell
docker run --rm -it --volume=$(pwd):/src amd64/python:3.6-slim-bullseye bash
python -m venv .venv
source .venv/bin/activate
cd /src
pip install -r requirements-test.txt
pytest --no-cov
```
