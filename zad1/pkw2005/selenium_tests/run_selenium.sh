#!/bin/bash

TESTS=`dirname $0`/pkw*.py

for i in ${TESTS[*]}; do
    echo "Testing "`basename "$i"`;
    python $i;
    if [ 0 -eq "$?" ]
    then
        echo "    OK"
    fi
done;
