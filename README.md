# codeowners

This was built for my Software Engineering Fundamentals Module (QAC020C125SS).

## Prerequisites

- Python 3.10 + installed
- A GitHub Organisation.
- Personal Access Token for GitHub Organisation, with Read/Write access.
- GitHub Organisation has a `.github` repository.

## Steps

### 1. Check Python Version

MacOS & Linux
```shell
python3 -V
```
Windows
```shell
python -V
```

### 2. Downlaod & update pip

MacOS & Linux
```shell
python3 -m ensurepip --upgrade
```
Windows
```shell
python -m ensurepip --upgrade
```

### 3. Clone this repository
```shell
git clone git@github.com:gabrielg2020/codeowners.git && cd codeowners
```

### 4. Setup Python Virtual Enviroment

MacOS & Linux
```shell
python3 -m venv .venv && source .venv/bin/activate
```
Windows
```shell
python -m venv C:\path\to\codeowners\.venv
```
```shell
C:\path\to\codeowners\.venv\Scripts\activate.bat
```

### 5. Install required packages

MacOS & Linux
```shell
pip3 install -r requirements.txt
```
Windows
```shell
pip install -r requirements.txt
```

### 6. Setup enviroment variables

MacOS & Linux
```shell
cp .env.dist .env && sed -i 's/tk/<REPLACE_ME_WITH_YOUR_TOKEN>/g' .env
```
Windows
```shell
copy .env.dist .env && powershell -Command "(Get-Content '.env') -replace 'tk','<REPLACE_ME_WITH_YOUR_TOKEN>' | Set-Content '.env'"
```

## Optional: Setting up unit tests.

### Clone testing repository

```shell
git clone git@github.com:codeowners-rfc-test/testing-repo.git
```

### Run `Pytest`

```shell
pytest
```

Error highlighting
```shell
pytest -vv --code-highlighting=yes
```

## Packages used

### `python-dotev`

Loads variables in `.env` into run-time enviroment variables.

### `pytest & pytest-mock`

Unit testing package and it's class mocking library.

### `logger`

Improved `info`, `warning` and `error` logging.

### `PyGitHub`

GitHub API v3 wrapper.

### `pylint`

Python linting.
