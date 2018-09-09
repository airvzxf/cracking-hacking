#!/usr/bin/python
# -*- coding: utf-8 -*-

from itertools import combinations


if __name__ == '__main__':
	
	wordList = [
		"Airv",
		"airv",
		"Zxf",
		"zxf",
		"Rovi",
		"rovi",
		"Lvvg",
		"lvvg",
		"30",
		"08",
		"83",
		"1983",
		"830830",
		"300883",
		"19830830",
		"30081983",
		"19831983",
		#~ "16",
		#~ "04",
		#~ "63",
		#~ "1963",
		#~ "630416",
		#~ "160463",
		#~ "19630416",
		#~ "16041963",
		#~ "19631963",
		"2468",
		"02468",
		"24680",
		"Banorte",
		"banorte",
		"Bqh",
		"Nabiki",
		"nabiki",
		" ",
		"!",
		"-",
		"-",
	]


	f = open("permutation-list.txt", "w")


	print "Working..."
	for w in range(0, len(wordList)+1):
		for c in combinations(wordList, w):
			#~ print(c)
			f.write( "".join(str(x) for x in c) )
			f.write( "\n" )


	print "All permutations have been created."
	f.close()

	print "Finished!"
