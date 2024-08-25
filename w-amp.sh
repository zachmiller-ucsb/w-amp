#!/bin/bash

# update to the desired kv size
value_size=512
key_size=16

gb_in_writes=$(( 10**9 / ($value_size + $key_size) ))
gb=50 # 50 GB on aws
write_ops=$(( $gb * $gb_in_writes )) 

T=5
mb=10 # 10 MB for base
base=$(( $mb*(10**6) ))

# db=/mnt/db_bench
db=/db_bench

./db_bench \
	--db=$db \
	--benchmarks=fillrandom,stats \
	-compression_type=none \
	-max_bytes_for_level_multiplier=$T \
	-num=$write_ops \
	-key_size=$key_size \
	-value_size=$value_size \
	-seed=1 \
	-max_bytes_for_level_base=$base \
	-bloom_bits=0 \
	-stats_dump_period_sec=10