#!/bin/bash -xv

FILE=c_print_something.c
EXEC=run
TEXT="Hellow darknes my old friend!"
TEXT_HACKED="This code was HACKED by mE!!!"

sudo rm -f ${EXEC}
gcc ${FILE} -o ${EXEC}
#gcc -O ${FILE} -o ${EXEC}
#gcc -g -Wall ${FILE} -o ${EXEC}

./${EXEC} "${TEXT}" &
PID=$!
echo "PID: ${PID}\n"

sleep 2
sudo ./read_write_heap.py ${PID} "${TEXT}" "${TEXT_HACKED}"
sleep 6

kill ${PID}
rm -f ${EXEC}
