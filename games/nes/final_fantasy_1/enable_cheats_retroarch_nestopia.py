#!/usr/bin/env python3

from sys import argv, exit


def print_usage():
	'''Print the usage string if script was used improperly'''
	print('Usage: \
		\t$ {} <pid>'.format(argv[0]))
	exit(1)


def read_write_heap(pid, enable='enable'):
	'''Replace the original opcodes to a new ones with hacks.'''
	is_set_enable = True if (str.lower(enable) == 'enable') else False
	print('pid: ' + pid)
	print('enable: ' + enable)
	print('is_set_enable: ', is_set_enable)
	print()

	opcodes = {
		'3CAEB': (b'\x8d\x50\xff', b'\x90\x90\x90')
	}

	try:
		maps_file = open('/proc/{}/maps'.format(pid), 'r')
	except IOError as e:
		print("Can't open file /proc/{}/maps: IOError: {}".format(pid, e))
		exit(1)

	memory_info = None

	for line in maps_file:
		if '/.config/retroarch/cores/nestopia_libretro.so' in line \
			and 'r-xp' in line \
			and '00000000' in line:
			memory_info = line.split()

	maps_file.close()
	print('memory_info:')
	print(memory_info)

	if not memory_info:
		print('No memory region found!')
		exit(1)

	addr = memory_info[0].split('-')
	print('addr: ', addr)
	print()

	for offset in opcodes:
		opcode_base, opcode_new = opcodes[offset]
		opcode_bytes = len(opcode_base)
		print(offset, opcodes[offset])
		print('opcode_base: ', opcode_base)
		print('opcode_new:  ', opcode_new)
		print('opcode_bytes:', opcode_bytes)
		print()

		try:
			mem_file = open('/proc/{}/mem'.format(pid), 'rb+')
		except IOError as e:
			print("Can't open file /proc/{}/maps: IOError: {}".format(pid, e))
			exit(1)

		memory_start = int(addr[0], 16)
		memory_end = int(addr[1], 16)
		memory_offset = int(offset, 16)
		print('memory_start:  ', memory_start)
		print('memory_end:    ', memory_end)
		print('memory_offset: ', memory_offset)
		print()

		mem_file.seek(memory_start + memory_offset)
		actual_opcode = mem_file.read(opcode_bytes)
		print('actual_opcode:   ', actual_opcode)

		if is_set_enable:
			if actual_opcode == opcode_new:
				print('Nothing to do, the opcode {} was set up.'.format(offset))
				break
			elif actual_opcode != opcode_base:
				print('Error, the opcode {} has a wrong address or opcodes.'.format(offset))
				break
		else:
			if actual_opcode == opcode_base:
				print('Nothing to do, the opcode {} was set up.'.format(offset))
				break
			elif actual_opcode != opcode_new:
				print('Error, the opcode {} has a wrong address or opcodes.'.format(offset))
				break

		mem_file.seek(memory_start + memory_offset)
		if is_set_enable:
			mem_file.write(opcode_new)
		else:
			mem_file.write(opcode_base)

		mem_file.seek(memory_start + memory_offset)
		data = mem_file.read(opcode_bytes)
		print('replaced opcode: ', data)
		print()

		mem_file.close()

if __name__ == '__main__':
	if (len(argv) == 3):
		pid = argv[1]
		enable = argv[2]
		read_write_heap(pid, enable)
	else:
		print_usage()
