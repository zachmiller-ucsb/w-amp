#!/bin/bash

grep "Sum" $1 | tr -s ' ' | cut -d ' ' -f4 -f5 -f13 > pruned_$1.txt