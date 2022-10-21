#!/bin/bash
python --version
python -m pip install --upgrade pip
pip3 install -r https://raw.githubusercontent.com/snowflakedb/snowflake-connector-python/v2.7.9/tested_requirements/requirements_39.reqs #requirements_39 because of Python version 3.9.7, make changes according to the version available
pip3 install snowflake-connector-python==2.8.0 # latest version recorded in September 2022