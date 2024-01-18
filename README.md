# uWSGI Flask Template
This repository is meant as a template for Python server endpoints that utilize nginx, uWSGI, and Flask. Many of my current web API projects use this code as a base, so I decided to create a universal repository to easily and quickly clone the code needed for new projects.

## Getting Started
A few files have project-specific text that needs to be changed:
- `project-name.service` - replace `<path/to/project>` with the full path to the template's directory  
- `project-name.py` - replace `<endpoint>` with the server route that is being proxied through uWSGI
- `wsgi.py` - Replace `<main-script-name>` with the main python script's name (`project-name.py` by default)
- `project-name.service` - Replace `<project-name>` and `<path/to/project>` with the project's name and the full path to the template's directory respectively

## Requirements
- A python virtual environment in a directory called `venv` is expected, with the following packages installed:
    - `asyncio`
    - `flask[async]`
    - `uwsgi`
    - `requests`
- Additionally, this project is meant to use an existing webserver such as nginx to route requests to the Flask server.

## Basic Usage
- Make all the required changes to files as listed above
- Create the Python virtual environment `venv` at the root of the project, installing required packages (alternatively copy an existing virtual environment that meets the project requirements)
- Enable and start the .service file to start the server
- Configure nginx (or another webserver) with uwsgi to route requests to the Flask server using the generated .sock file
