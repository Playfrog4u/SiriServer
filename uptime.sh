#!/bin/sh




pd=`ps -ef | awk '/[s]iriServer/ { print $2 }'`
expr $(awk '{print $1}' FS=\. /proc/uptime) - $(awk '{printf ("%10d\n",$22/100)}' /proc/$pd/stat)