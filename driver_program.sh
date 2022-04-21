#!/bin/bash

# Runs the python code
login() {
    python wifi.py
    status=$?

    # notify whether the login was successful or not
    if [[ status -eq 0 ]]
    then notify-send "Internet connection restored"
    else notify-send "Login unsuccesful"
    fi
}

# checks every 5 second if login is required or not
while true
do
    # store the response status in result 
    result=$(curl -s -o /dev/null -w %{http_code} http://networkcheck.kde.org/)
    
    if [[ $result -eq 303 ]]
    then login
    fi
    sleep 5
done
