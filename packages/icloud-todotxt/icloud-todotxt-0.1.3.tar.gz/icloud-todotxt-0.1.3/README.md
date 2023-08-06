<p align="center"><h1 align="center">iCloud todo.txt</h1></p>

<p align="center"><em>Synchronize your local `todo.txt` with iCloud.</em></p>

<p align="center">
<img src="https://raw.githubusercontent.com/DavidHeresy/icloud-todotxt/main/public/pylint.svg" alt="Linting: pylint">
<a href="https://github.com/psf/black" target="_blank">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">
</a>
<!-- TODO: Add PyPi badge. -->
<!-- TODO: Add licencse badge. -->
<!-- TODO: Add GitHub stars badge. -->
</p>

## Requirements

On your local machine, you have to set the following two environment variables.

```bash
TODO_FILE="path/to/your/todo.txt"
APPLE_ID="<Your Apple ID email address.>"
```

On iCloud you need a folder called `ToDo` where the `todo.txt` will live.

## Installation

Install the package with pip

```bash
pip install --user path/to/dist/icloud_todotxt-0.1.0-py3-none-any.whl
```

or pipx

```bash
pipx install path/to/dist/icloud_todotxt-0.1.0-py3-none-any.whl
```

## Usage

Before you can use the tool, you have to login once into iCloud.

```bash
icloud --username=$APPLE_ID
```

Download the `todo.txt` from iCloud.

```bash
icloud-todotxt download
```

Upload the `todo.txt` to iCloud.

```bash
icloud-todotxt upload
```

## Internal Dependencies

* [pyiCloud](https://github.com/picklepete/pyicloud)
* [Typer](https://typer.tiangolo.com/)
