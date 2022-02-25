# Welcome to PyPass

A Python password manager and generator based mainly for command-line usage.

## FAQ

### What is PyPass?

PyPass is a password manager and password generator made with python. It currently only supports CLI interfaces but may support GUI in the future.

### How secure is PyPass?

Currently, it is as secure as the python `random.SystemRandom` function. I don't know how secure that is, but I presume not very.

### Can I contribute to PyPass?

Sure! Any help is appreciated. 
See the [Contribution Section](https://github.com/LemonHeadOnGit/PyPass/blob/dev/readme.md#contribution) for more information.

## Installation

PyPass comes with some libraries that make development easier.
It is recommended to setup a **Virtual Environment or `venv`** before installing these libraries for development.

Once ready, you can simply `cd` into the root project directory, and run:

```bash
# Install python packages in current directory

pip install .
```

This will run the `setup.py` file located in the root of the directory.
If at any point you need to "update" or "upgrade" the modules, you can simply run:

```bash
# Upgrade the pip modules

pip install --upgrade .
```

> TODO [#2](https://github.com/LemonHeadOnGit/PyPass/issues/2)

## Contribution

> TODO [#2](https://github.com/LemonHeadOnGit/PyPass/issues/2)

If you want to contribute go ahead!

> NOTE: Most pull requests will need to be thoroughly checked, especially if the code modifies the encryption part of the project.
