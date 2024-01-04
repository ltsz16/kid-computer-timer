#!/bin/bash

# Specify the application name
application_name="your_application.exe"

# Check if the application is running
if pgrep -i "$application_name" > /dev/null ; then
  echo "Application is running. No action needed."
else
  echo "Application is not running. Shutting down the computer."
  shutdown /s /t 1
fi
