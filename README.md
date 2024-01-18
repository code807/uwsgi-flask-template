# uWSGI Flask Template
This repository is meant as a template for http/https webserver endpoints that utilize nginx, uWSGI, and Flask. This template is intended for Linux servers running systemd. Many of my current web API projects use this code as a base, so I decided to create a universal repository to easily and quickly clone the code needed for new projects.

## Getting Started
A few files have project-specific text that needs to be changed:
- `project-name.service` - replace `<path/to/project>` with the full path to the template's directory  
- `project-name.py` - replace `<endpoint>` with the server route that is being proxied through uWSGI
- `wsgi.py` - Replace `<main-script-name>` with the main python script's name (`project-name.py` by default)
- `project-name.service`
    - Replace `<project-name>` with the project's name
    - Replace `<path/to/project>`  with the full path to the template's directory
    - Replace `<user>` with the name of the Linux user the service will be run as (the same user must have access to the template's directory)

## Requirements
- A python virtual environment in a directory called `venv` is expected, with the following packages installed:
    - `asyncio`
    - `flask[async]`
    - `uwsgi`
    - `requests`
- Additionally, this project is meant to use an existing webserver such as nginx to route requests to the Flask server.

## Basic Usage
- Make all the required changes to files as listed above
- Create the Python virtual environment `venv` at the root of the project, installing required packages
- Enable and start the .service file to start the server
- Configure nginx (or another webserver) with uwsgi to route requests to the Flask server using the generated .sock file

## Advanced Instructions
### Setting up a Python virtual environment
- Navigate to the project's root directory in a terminal
- Run `python -m venv venv`
- Enter the virtual environment
    - bash/zsh: `source <venv>/bin/activate`
    - PowerShell: `<venv>/bin/Activate.ps1`
- Update pip by running `pip install --upgrade pip`
- Install required packages by running `pip install asyncio flask[async] uwsgi requests`

More details can be found in the [Python Docs](https://docs.python.org/3/library/venv.html)
### Enabling systemd service file (with sudo priviledges)
- Move the .service file from the project's directory to `/etc/systemd/system`
- Run `sudo systemctl enable project-name` replacing project-name with the name of the service file sans the extension
- Run `sudo systemctl restart project-name` to start the service