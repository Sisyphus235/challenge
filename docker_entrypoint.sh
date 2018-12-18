#!/usr/bin/env bash

exec gunicorn --workers 3 \
--bind 0.0.0.0:5003 \
run:app

"$@"