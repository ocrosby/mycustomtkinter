# My CustomTkinter

An example repo for CustomTkinter exploration.

## Setup

Create a virtual environment with Python 3.13:

```bash
python3.13 -m venv .venv
```

Upgrade pip

```bash
source .venv/bin/activate
pip install --upgrade pip
````

Configure the Python interpreter in PyCharm:

- Open PyCharm
- Go to Preferences > Project: mycustomtkinter > Python Interpreter
- Click the gear icon and select Add ...
- Choose Existing environment
- Navigate to the .venv/bin/python interpreter
- Click OK

At this point opening a new terminal should show the virtual environment is active.

## Installation


Install invoke:

```bash
source .venv/bin/activate
pip install invoke
```

Use invoke to install the dependencies:

```bash
source .venv/bin/activate
invoke install
```
