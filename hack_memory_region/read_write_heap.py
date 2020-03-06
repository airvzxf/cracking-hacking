#!/usr/bin/env python3

from sys import argv, exit


def print_usage():
	'''Print the usage string if script was used improperly'''
	print('Usage: \
		\t$ {} <pid> <string to read> <string to write>'.format(argv[0]))
	exit(1)


def read_write_heap(pid, read_str, write_str):
	'''Find @read_str in the heap of @pid and replace it with @write_str'''

	print('pid: ' + pid)
	print('read_str: ' + read_str)
	print('write_str: ' + write_str)

	try:
		maps_file = open('/proc/{}/maps'.format(pid), 'r')
	except IOError as e:
		print("Can't open file /proc/{}/maps: IOError: {}".format(pid, e))
		exit(1)

	heap_info = None

	for line in maps_file:
		if 'heap' in line:
			heap_info = line.split()

	maps_file.close()
	print('heap_info:')
	print(heap_info)

	if not heap_info:
		print('No heap found!')
		exit(1)

	addr = heap_info[0].split('-')
	perms = heap_info[1]
	print('addr: ', addr)
	print('perms: ' + perms)

	if 'r' not in perms or 'w' not in perms:
		print('Heap does not have read and/or write permission')
		exit(0)

	while True:
		try:
			mem_file = open('/proc/{}/mem'.format(pid), 'rb+')
		except IOError as e:
			print("Can't open file /proc/{}/maps: IOError: {}".format(pid, e))
			exit(1)

		heap_start = int(addr[0], 16)
		heap_end = int(addr[1], 16)
		mem_file.seek(heap_start)
		heap = mem_file.read(heap_end - heap_start)
		is_text_found = heap.count(bytes(read_str, 'ASCII'))
		print('is_text_found: ', is_text_found)

		if is_text_found == 0:
			break

		str_offset = heap.find(bytes(read_str, 'ASCII'))
		print('str_offset: ', str_offset)

		str_result = heap[str_offset - 2 : str_offset + len(read_str) + 2]
		print('str_result: ', str_result)

		mem_file.seek(heap_start + str_offset - 2)
		data = mem_file.read(len(read_str) + 3)
		print('Found:   ', data)

		mem_file.seek(heap_start + str_offset)
		mem_file.write(bytes(write_str, 'ASCII'))
		#mem_file.write(str.encode(write_str))

		mem_file.seek(heap_start + str_offset - 2)
		data = mem_file.read(len(read_str) + 3)
		print('Replaced:', data)

		mem_file.close()

if __name__ == '__main__':
	if (len(argv) == 4):
		pid = argv[1]
		search_str = argv[2]
		replace_str = argv[3]
		read_write_heap(pid, search_str, replace_str)
	else:
		print_usage()

