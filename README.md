# lpc character generator

- Pillow
- numpy
- black (code formatter)

## Development

### pyenv (optional)

Recommend using pyenv to manage your python version.

- Pre-requisites: https://github.com/pyenv/pyenv/wiki/Common-build-problems#prerequisites
- Installer: https://github.com/pyenv/pyenv-installer

### Poetry

Replacement for pip and virtualenv. Manages dependencies and virtual environments.

- Installer: https://python-poetry.org/docs/#installation

#### Adding a package:

```bash
poetry add Pillow numpy
```

_Package definition can be found in `pyproject.toml` and the automatically resolved versions are found in `poetry.lock`._

#### Activating environment:

```bash
poetry shell
python my_script.py
```

#### Simple end-to-end test:

```bash
poetry shell
pytest -s
```
