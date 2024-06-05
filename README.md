# General

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
- Upgrade the pip tool to the newest version: `$PYTHON_EXECUTABLE -m pip install --upgrade pip`
- Install the [poetry](https://python-poetry.org/) tool: `$PYTHON_EXECUTABLE -m pip install --user poetry`
- Open the project in VSCode.
- Inside VSCode, open a terminal and install the project dependencies: `$PYTHON_EXECUTABLE -m poetry install`. This creates a virtual environment for the project which has all of the required Python packages installed.
- Now, select the Python interpreter installed in the virtual environment as the default Python interpreter for the workspace. In order to do this, open VSCode's command pallette with `CTRL+SHIFT+p` and select `Python: Select Interpreter`. Afterwards, select the correct Python interpreter. From now on, every time you open a terminal within this workspace inside VSCode, the virtual environment is automatically activated. Also, only by setting the correct Python interpreter for the workspace launching the Django app in debugging mode works.
- Finally, inside a terminal that has the virtual environment activated, run `pre-commit install --install-hooks --hook-type pre-commit --hook-type pre-merge-commit` to install git hooks. **It's crucial for you to install these git hooks in order to ensure code quality**. (see [Code Quality](#code-quality)).

### Project Structure

#### Directories

- `devsearch/`: Core package of Django application.
- `apps/`: Django apps. Contains one subfolder for each Django app.
- `docs/`: Project documentation files.
- `tests/`: Test code.
- `pre_commit_hooks/`: Custom hooks used by the pre-commit tool.
- `.github/workflow/`: YAML configuration for Github workflows.
- `.vscode/`: Configuration files for VSCode.
- `.git/`: git directory.

#### Files

- `manage.py`: Django application management script.
- `pyproject.toml`: Configuration file read by [poetry](https://python-poetry.org/) tool. The file contains the installation requirements.
- `poetry.lock`: Configuration file read by [poetry](https://python-poetry.org/) tool. This file contains the exact Python package versions to install.
- `.pep8`: Configuration file read by Python code formatting tool [autopep8](https://pypi.org/project/autopep8/).
- `.pre-commit-config.yaml`: Configuration read by [pre-commit](https://pre-commit.com/) tool.
- `.prettierrc`: Configuration file read by code formatting tool [prettier](https://prettier.io/).
- `isort.cfg`: Configuration file ready by Python import sorting tool [isort](https://pycqa.github.io/isort/).
- `mypy.ini`: Configuration file read by Python static type checker [mypy](https://mypy.readthedocs.io/en/stable/).
- `.pylintrc`: Configuration file read by Python linting tool [pylint](https://pypi.org/project/pylint/).
- `pytest.ini`: Configuration file read by Python testing framework [pytest](https://docs.pytest.org/en/8.2.x/).
- `.gitignore`: gitignore file.

### Code Quality

The code quality of this project is ensured with various code formatting and code analysis tools:

- [autopep8](https://pypi.org/project/autopep8/): Python code formatter. Adheres to [PEP 8](https://peps.python.org/pep-0008/) standard.
- [prettier](https://prettier.io/): Code formatter. Used in this project to format all files except for Python files.
- [isort](https://pycqa.github.io/isort/): Sorting of Python import statements.
- [mypy](https://mypy.readthedocs.io/en/stable/): Static type code checker for Python.
- [pylint](https://pypi.org/project/pylint/): Static code analysis tool for Python.
- [pytest](https://docs.pytest.org/en/8.2.x/): Python testing framework (see also [`python-django`](https://pytest-django.readthedocs.io/en/latest/)).

These tools, amoung other checks, are automatically applied as pre-commit hooks upon each call of `git commit` or `git merge` by the [pre-commit](https://pre-commit.com/) tool. The hooks take care of formatting the code, running type checks as well as running unit tests and automatically detecting and fixing some other potential issues. If any of the hooks throw an error (i.e. exit status code is not equal to 0), the changes are not committed to the local git repository.

For this project we chose to apply all of the above mentioned tools with their default configurations. However, specific configuration needs may arise at some point. For this case, each tool has its own configuration file that can be used to customize its behaviour (see [Project Structure -> Files](#files)).

### Development Workflow

The git development workflow used for this project is the widely used _Github Flow_. It is much simpler than the other widely used [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/) method, and an especially good fit for web application projects with short release cycles. [This video](https://www.youtube.com/watch?v=hG_P6IRAjNQ&ab_channel=AlexHyett) makes a concise comparison of the two.

The Github flow for the `devsearch` project works like this:

- The local and remote [devsearch](https://github.com/thomas-salzmann/devsearch) repository have a protected main branch.
- This means that developers can not commit locally to the `main` branch or push to the remote `main` branch.
- The remote `main` branch evolves by accepted pull requests that result in a merge-commit of another remote branch.
- The local `main` branch evolves by pulling from the remote `main` branch.

To summarize, this is how your git workflow looks like as a developer on this project.

- First clone the [devsearch](https://github.com/thomas-salzmann/devsearch) repository and follow the [Installation steps](#installation).
- Create a new branch `new_branch`, switch to this branch, develop your code and commit your changes to `new_branch`.
- When you are done with the work `new_branch`, go back to the `main` branch and pull the remote `main` branch to have the latest updates implemented by other developers on the team locally available.
- Switch back to `new_branch` and merge the `main` branch. Resolve potential merge conflicts in `new_branch`.
- Generally, it is recommended you pull the `main` branch regularly and merge it into `new_branch` even while still developing it.
- Push `new_branch` to the remote repository on Github and create a pull request for remote `new_branch` to be merged into remote `main`.
- After creating the pull request, do not commit or push any further changes to `new_branch` unless the pull request is rejected and correcting changes need to be made.
- After the pull request is accepted, do three things
  1.  Pull the remote `main` branch into the local `main` branch and merge the changes into the branch you currently work on.
  2.  Delete the local `new_branch`.
  3.  Delete the reference of remote `new_branch` in local repository by `git remote update origin --prune`.
- For your next piece of work, switch to the `main` branch, delete local `new_branch` and create another branch `new_branch_2`.
- Upon creating the pull request, a CI / CD pipeline is triggered (**Note: this is yet to be implemented**).
- If it exeuctes without any errors, the pull request is automatically accepted and the remote `new_branch` is merged with the remote `main` branch.
- If errors occur, the pull request is rejected and correcting changes need to be made.
- After the remote branch is merged, it is deleted from the remote repository to keep the repository clean. This is Github flow best practice (read [here](https://docs.github.com/en/get-started/using-github/github-flow#delete-your-branch)).

We adhere to the following naming conventions for our git branches:

1. Each branch name starts with a category word followed by a forward slash.

   | Category | Description                                                                                           |
   | -------- | ----------------------------------------------------------------------------------------------------- |
   | feature  | Feature branches, i.e. code that ships new features.                                                  |
   | deploy   | Code associated with deployment of the project (Docker, Kubernetes, Terraform, Github Actions, etc.). |
   | qa       | Code written to enhance quality (pre-commit hooks, writing test cases, code refactoring, etc.).       |
   | bugfix   | Non-critical bug fixes of the code.                                                                   |
   | hotfix   | Critical high priority bug fixes that needed to be shipped into production as quickly as possible.    |
   | task     | Any other type of task that does not belong in the other categories (e.g. updating documentation).    |

2. After the forward slash, describe what the branch does with a concise, yet clear name. Let's call this the _branch descriptor_

3. Use lowercase letters for the branch descriptor only.

4. Use hyphens ('-') to separate words in the branch descriptor.

5. Make sure the combination of category and branch descriptor is unique. There may not be two branches with the same name in a git repository. In this project, we use an increment counter for each category at the beginning of the branch descriptor. The increment counter starts counting at '1'.

   **Note**: For larger teams using product management software to track ticket numbers, the ticket number can be used at the beginning of the branch descriptor to make it unique. The more developers work on a project, the more crucial a clear and standardized git naming convention is to maintain organization and facilitate collaboration.

Some examples of valid branch names are:

- feature/1-add-projects-page
- feature/2-add-user-account-management
- deploy/1-setup-dockerfile
- deploy/2-setup-kubernetes-file
- qa/1-setup-pre-commit-hooks
- qa/2-add-pre-commit-hook-to-protect-local-main-branch
- task/1-update-docs-README
- task/2-update-docs-README
