import os
import time
import subprocess
from multiprocessing import Process
import sys

def KeepConnection(stub):
	while 1:
		time.sleep(120)
		print("continuing")

if __name__ == '__main__':

	p = Process(target=KeepConnection, args=("",))
	p.daemon = True
	p.start()

	f = open("AutumnLog_aws.txt", "a")  # append mode

	# update to the desired kv size
	valueSize = 100
	keySize = 16


	write_ops = 8620689 # 8620689 * 116 Bytes = 1 GB
	write_ops *= 10 # 10 GB on aws 

	read_ops = 10000
	sleepTime = 0
	seqNum = 0

	T = 3
	mb = 10
	base = mb * 1048576 # 10 MB for base

	local = True
	if local:
		#fix db size and k. vary c
		for c in [0.9, 0.8, 0.7, 0.6, 0.5]:
			result = subprocess.run(['./db_bench', '--benchmarks=fillrandom,waitforcompaction,stats',\
									'-max_bytes_for_level_multiplier='+str(T),\
									'-writes='+str(write_ops),\
									'-value_size='+str(valueSize),\
									'-seed=1',\
									'-autumn_c='+str(c),
									'-max_bytes_for_level_base='+str(base)], capture_output=True)
			f.write(result.stdout.decode('utf-8'))
			f.write('\n')
			print(result.stdout.decode('utf-8'))
			print("stderr:", result.stderr)

			# random point reads
			result = subprocess.run(['./db_bench', '--benchmarks=readrandom,stats',\
									'-max_bytes_for_level_multiplier='+str(T),\
									'-use_existing_db=true',\
									'-reads='+str(read_ops),\
									'-value_size='+str(valueSize),\
									'-seed=1',\
									'-autumn_c='+str(c),\
									'-max_bytes_for_level_base='+str(base)], capture_output=True)
			f.write(result.stdout.decode('utf-8'))
			f.write('\n')
			print(result.stdout.decode('utf-8'))

			# small range scan
			result = subprocess.run(['./db_bench', '--benchmarks=seekrandom,stats',\
									'-max_bytes_for_level_multiplier='+str(T),\
									'-use_existing_db=true',\
									'-reads='+str(read_ops),\
									'-value_size='+str(valueSize),\
									'-seed=1',\
									'-autumn_c='+str(c),\
									'-seek_nexts=10',
									'-max_bytes_for_level_base='+str(base)], capture_output=True)
			f.write(result.stdout.decode('utf-8'))
			f.write('\n')
			print(result.stdout.decode('utf-8'))

			# long range scan
			result = subprocess.run(['./db_bench', '--benchmarks=seekrandom,stats',\
									'-max_bytes_for_level_multiplier='+str(T),\
									'-use_existing_db=true',\
									'-reads='+str(read_ops),\
									'-value_size='+str(valueSize),\
									'-seed=1',\
									'-autumn_c='+str(c),\
									'-seek_nexts=100',
									'-max_bytes_for_level_base='+str(base)], capture_output=True)
			f.write(result.stdout.decode('utf-8'))
			f.write('\n')
			print(result.stdout.decode('utf-8'))


			seqNum += 1
			f.write('****************************************************************************\n')

	f.close()
	exit()
