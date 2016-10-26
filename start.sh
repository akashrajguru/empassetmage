#!/bin/bash
#fuser -k -n tcp 9090 && \
#python app.py


retfunce()
{
	fuser -k -n tcp 9090
	echo "process killed"
}

exitfunc()
{
	python app.py
	echo "application started"
}

retfunce
exitfunc