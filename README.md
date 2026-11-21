# Izutsu Browser

Izutsu is a language learning plus International Studies focused browser aim to help foreign languages, International Relations and Foreign Trade students, professionals, practisioners and enthusiasts to browse the internet in a structured way, as the application was specifically crafted for their educational and professional needs.

## Architectural principles

Initial folder structure and architecture:


    izutsu/
    │
    ├── izutsu/
    │   ├── __init__.py
    │   ├── __main__.py
    │   ├── config.py
    │   │
    │   ├── presentation/
    │   ├── browser/
    │   ├── application/
    │   ├── domain/
    │   │
    │   └── infrastructure/
    │       ├── database/
    │       │   ├── base.py
    │       │   ├── session.py
    │       │   └── models.py
    │       │
    │       └── platform/
    │
    ├── resources/
    ├── tests/
    ├── docs/
    ├── scripts/
    ├── migrations/
    ├── pyproject.toml
    └── README.md

### Main The architectural distinction

`domain/` This directory contains business concepts and rules

`application/` This directory will coordinate use cases

`infrastructure` This directory will contain technical implementations

This is the core separation of concerns in the application and it will become increasingly valuable as Izutsu grows.

## Configuring the Python Project

Create `pyproject.toml` in the project root

```

[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "izutsu"
version = "0.1.0"
description = "An educational browser for language learning and research."
requires-python = ">=3.12"
dependencies = [
    "PySide6",
    "SQLAlchemy>=2.0",
    "alembic",
    "pydantic",
    "platformdirs",
    "httpx",
]

[project.optional-dependencies]
dev = [
    "pytest",
    "pytest-qt",
]

[tool.setuptools.packages.find]
where = ["."]
include = ["izutsu*"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]

```

And then install the project in editable mode:

```
pip install -e ".[dev]"
```

This means you can import `izutsu` from anywhere within the development environment, and changes to your source code are immediately reflected without reinstalling the package.

