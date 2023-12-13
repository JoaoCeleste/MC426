#!/usr/bin/env bash
python3 -m flask db upgrade
python3 -u -m flask run --host=0.0.0.0