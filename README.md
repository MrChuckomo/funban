# FUNban

A fun and Flask-web-based [Kanban](https://en.wikipedia.org/wiki/Kanban_board) board!


# Development

## Create `conda` Environment

```bash
# List your python envs
$ conda env list

# Create new python envs
$ conda env create --prefix ./ops/pyenv/funban_env --file ./environment.yml

# Init your shell to use conda activate
$ conda init
$ conda init zsh

# Activate your new created python env
$ conda activate ./ops/pyenv/funban_env

# Show installed Python packages
$ conda list
```

## Run Webapp

```bash
# Using gunicorn debugging
$ gunicorn -b :5050 index:app --reload

# Using Flask built-in debugging
$ python run.py
```

Call the Website URL on your browser of choice: [http://localhost:5050/](http://localhost:5050/)
