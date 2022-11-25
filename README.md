# poetry_deps
Poetry dependency file browser

This project is inspired by Reactor assignment for trainees 2022.
I was not able to meet the deadline but decided to finish the project anyway.

About this app:

Poetry is a tool for dependency management and packaging in Python. Poetry uses lockfile to record which packages a project needs and which dependencies those packages have.

This app takes poetry.lock file and presents dependancies in a browser via HTML user interface. Parsing lockfile has been made from scratch without any ready-made 3rd party parsers. Sample input file is the lockfile of Poetry itself.

Basic functionality is deployed at:
https://poetry-deps.azurewebsites.net/
