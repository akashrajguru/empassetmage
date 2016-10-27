#!/bin/bash
#fuser -k -n tcp 9090 && \
#python app.py

retfunce(){
	fuser -k -n tcp 9090
	echo "process killed"
}

# Install supervisor configs
#if [ ! -f "/bin/supervisord.conf" ]; then 
#	echo_supervisord_conf > /bin/supervisord.conf; 
#fi

# add this program to the supervisor configs
#echo '
#[program:app]
#command=bash -c "python app.py"
#' >> /etc/supervisord.conf


# if supervisor already running, 'update' to add the new process
#pgrep supervisord > /dev/null || supervisord
#supervisorctl update
exitfunc(){

	python app.py &
	echo "application started" 
	exit 0
}
retfunce
exitfunc