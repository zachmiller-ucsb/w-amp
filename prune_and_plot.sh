#!/bin/bash

if [ $# -ne 3 ]; then
    echo "Usage: $0 LOG_ROCKSDB LOG_0.6 LOG_0.8"
    exit 1
fi

grep "Sum" $1 | tr -s ' ' | cut -d ' ' -f4 -f5 -f10 -f13 > wamp_$1.txt
grep "Sum" $2 | tr -s ' ' | cut -d ' ' -f4 -f5 -f10 -f13 > wamp_$2.txt
grep "Sum" $3 | tr -s ' ' | cut -d ' ' -f4 -f5 -f10 -f13 > wamp_$3.txt

sed -n '/Sum/{x;1!p;}; h' $1| sed 's/^[^0-9]*\([0-9]*\).*/\1/' > levels_$1.txt
sed -n '/Sum/{x;1!p;}; h' $2| sed 's/^[^0-9]*\([0-9]*\).*/\1/' > levels_$2.txt
sed -n '/Sum/{x;1!p;}; h' $3| sed 's/^[^0-9]*\([0-9]*\).*/\1/' > levels_$3.txt

grep "nvme1n1" $1_iostat | tr -s ' ' | cut -d ' ' -f7 > writes_$1.txt
grep "nvme1n1" $2_iostat | tr -s ' ' | cut -d ' ' -f7 > writes_$2.txt
grep "nvme1n1" $3_iostat | tr -s ' ' | cut -d ' ' -f7 > writes_$3.txt

python plot.py wamp_$1.txt levels_$1.txt writes_$1.txt wamp_$2.txt levels_$2.txt writes_$2.txt wamp_$3.txt levels_$3.txt writes_$3.txt

rm wamp_$1.txt levels_$1.txt writes_$1.txt wamp_$2.txt levels_$2.txt writes_$2.txt wamp_$3.txt levels_$3.txt writes_$3.txt