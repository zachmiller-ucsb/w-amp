#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 LOG_ROCKS LOG_0.6"
    exit 1
fi

grep "Sum" $1 | tr -s ' ' | cut -d ' ' -f4 -f5 -f13 > output1.txt
grep "Sum" $2 | tr -s ' ' | cut -d ' ' -f4 -f5 -f13 > output2.txt

python plot.py output1.txt output2.txt

rm output1.txt output2.txt