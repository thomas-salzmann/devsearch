""" Cleanup hook

This hook is executed last on each run of the 'pre-commit' tool.
The corresponding pre-commit configuration file is ../.pre-commit-config.yaml.
"""

import shutil
from pathlib import Path


def remove_directories():
    """" Remove directories. """
    parent_dir = Path(__file__).resolve().parent.parent
    directories = ['.mypy_cache', '.pytest_cache', 'node_modules']

    for directory in directories:
        dir_path = parent_dir / directory
        if dir_path.exists():
            try:
                shutil.rmtree(dir_path)
            except FileNotFoundError:
                pass


def main() -> int:
    """ Main function. """
    remove_directories()

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
