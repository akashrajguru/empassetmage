#!/bin/bash

fuser -k -n tcp 9090 && \
python app.py