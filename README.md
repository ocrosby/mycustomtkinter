# My CustomTkinter

An example repo for CustomTkinter exploration.

## Setup

First ensure tcl-tk is installed:

```bash
brew install tcl-tk
brew install python-tabulate
```

Then install uv:

```bash
pip install uv
```

To create the project I initialized it with uv:

```bash
uv init
```

Create a new virtual environment with uv:

```bash
uv .venv -p python3.13
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Configure the Python interpreter in PyCharm:

- Open PyCharm
- Go to Preferences > Project: mycustomtkinter > Python Interpreter
- Click the gear icon and select Add ...
- Choose Existing environment
- Navigate to the .venv/bin/python interpreter
- Click OK

At this point opening a new terminal should show the virtual environment is active.

## Installation

```bash
uv add customtkinter
```
