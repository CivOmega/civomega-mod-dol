# CivOmega: Question Module Bootstrap

This is a dummy module for [CivOmega](https://github.com/CivOmega/civomega). CivOmega Modules are what connect datasets and APIs to question patterns.

Note: This repository is where you should start if you want to allow people to ask questions about a dataset or API that doesn't exist in CivOmega already.  If you're actually interested in adding more questions to a dataset that already exists, we suggest that you contribute to an existing module instead of creating a new one from the ground up.

Modules have the following components:

- [parsers.py](comod_example/parser.py) - this is where you define question routes and answer logic
- [patterns.py](comod_example/patterns.py) - this is where you define the list of question patterns that your module knows how to answer
- [templates](comod_example/templates) - this is where you define the output format for your answers

## Creating a Module

Read the [CivOmega Module documentation](https://github.com/CivOmega/civomega/blob/develop/doc/MODULES.md) to understand how to use this boilerplate to develop a new module.
