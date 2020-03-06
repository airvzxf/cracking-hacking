#!/bin/bash -vx

PID=$(pidof retroarch)
echo "PID: ${PID}"

sudo ./enable_cheats_retroarch_nestopia.py ${PID} 'Enable'
