import sys
from pathlib import Path

import pytest

EXAMPLES_DIR = Path(__file__).parent / "examples"
EXAMPLE_NAMES = tuple(
    p.name for p in EXAMPLES_DIR.iterdir() if not p.name.startswith((".", "_"))
)


@pytest.fixture(scope="session", autouse=True)
def add_pypath():
    "Add example modules to the python path"
    sys.path.insert(0, str(EXAMPLES_DIR))
    yield
    sys.path.remove(str(EXAMPLES_DIR))


@pytest.fixture(autouse=True)
def undo_examples_import():
    "Undo any imports of example modules"
    yield
    to_remove = [
        name for name in sys.modules if name.startswith(EXAMPLE_NAMES)
    ]
    for name in to_remove:
        del sys.modules[name]
