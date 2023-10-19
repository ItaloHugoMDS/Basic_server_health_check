# Basic_server_health_check
A python script that can be run to check for basic status of the health of the up running server.

This script will check for CPU overload, disk space availability, memory availability and server resolution into '127.0.0.1'. In case any error occur, an email will be sent through SMTP service stating the problem and asking to check on the machine.

This script is idempotent and can be set to be ran by cron service on any linux based server.
