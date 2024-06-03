# General

This is a demo project currently in progress. It will be completed by Monday, 10th of June 2024.

The purpose of this project is to demonstrate my skills with the Python / Django technology stack.

The project developed is a platform to search for developers, hence the name **devsearch**.

# How To Use This Project?

## As a User

If you are a regular user (i.e. you simply want to use the project), go to the [registration page]() to create an account or [login]() if you already have an account.

## As a Contributor / Developer

### Installation

- Clone the repository via `git clone git@github.com:thomas-salzmann/devsearch.git`
- In order for this to work, make sure that the repo owner *thomas.salzmann.privat@gmail.com* has added you as a collaborator for this repository on Github. Also make sure that you've added your public SSH Key to your Github account.
- VSCode is the recommended code editor to contribute to this project.
- Make sure Python is installed on your operating system.
- If not already the case, add the parent directory of your Python executable file to the `PATH` environment variable.
- In the following, for Linux and Mac systems, `$PYTHON_EXECUTABLE` has the value `python3`, whereas for Windows systems it has the value `$python`.
- Upgrade the _pip_ tool to the newest version: `$PYTHON_EXECUTABLE -m pip install --upgrade pip`
- Install the _pipenv_ tool: `$PYTHON_EXECUTABLE -m pip install --user pipenv`
- Open the project in VSCode.
- Inside VSCode, open a terminal and install the project dependencies: `$PYTHON_EXECUTABLE -m pipenv install --dev`. This creates a virtual environment for the project which has all of the required Python packages installed.
- Now, select the Python interpreter installed in the virtual environment as the default Python interpreter for the workspace. In order to do this, open VSCode's command pallette with `CTRL+SHIFT+p` and select `Python: Select Interpreter`. Afterwards, select the correct Python interpreter. From now on, every time you open a terminal within this workspace inside VSCode, the virtual environment is automatically activated. Also, only by setting the correct Python interpreter for the workspace launching the Django app in debugging mode works.
- Finally, inside a terminal that has the virtual environment activated, run `pre-commit install --install-hooks --hook-type pre-commit --hook-type pre-merge-commit` to install git hooks. **It's crucial you install these git hooks to ensure code consistency and a high code quality**. The hooks take care of formatting the code, running type checks as well as running unit tests and automatically detecting and fixing some other potential issues. The project uses Python's `pre-commit` package ([Documentation](https://pre-commit.com/), [Supported Hooks](https://pre-commit.com/hooks.html), [Git Hooks Documentation](https://git-scm.com/docs/githooks)).

### Code Quality

The code quality of this project is ensured with various code formatting and code analysis tools:

- [`autopep8`](https://pypi.org/project/autopep8/): Python code formatter. Adheres to [PEP 8](https://peps.python.org/pep-0008/) standard.
- [`prettier`](https://prettier.io/): Code formatter. Used in this project to format all files except for Python files.
- [`isort`](https://pycqa.github.io/isort/): Sorting of Python import statements.
- [`mypy`](https://mypy.readthedocs.io/en/stable/): Static type code checker for Python.
- [`pylint`](https://pypi.org/project/pylint/): Static code analysis tool for Python.
- [`pytest`](https://docs.pytest.org/en/8.2.x/): Python testing framework (see also [`python-django`](https://pytest-django.readthedocs.io/en/latest/)).

These tools, amoung other checks, are automatically applied upon each call of `git commit` or `git merge` by the `pre-commit` tool whose configuration file is `.pre-commit-config.yaml`. If any of them throws an error, the changes are not committed to the local repository.

For this project we chose to apply all of these tools with their default configurations. However, specific configuration needs may arise at some point. For this case, each tool has its own configuration file that can be used to customize its behaviour:

- `autopep8`: .pep8
- `prettier`: .prettierrc
- `isort`: isort.cfg
- `mypy`: mypy.ini
- `pylint`: .pylintrc
- `pytest`: pytest.ini

### Development Workflow
