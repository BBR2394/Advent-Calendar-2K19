# -*- coding: utf-8 -*-
# @Author: Baptiste
# @Date:   2019-12-01 22:18:06
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-12-02 00:13:47

#!/usr/local/bin/python3

import math
from Module import * 

def open_a_file(file_name):
	try:
		fd = open(file_name, 'r')
		print("-> The file is opened")
		return fd
	except  :
		print("=> an error occured when opening the file")
		return -1

def store_file_in_list(fd):
	lst = []
	line = fd.readline()
	entrynb = 1
	#print(":" + str(entrynb) + "> line juts to test " + str(line))
	while line != "":
		lst.append(int(line))
		line = fd.readline()
		entrynb += 1
		#print(":" + str(entrynb) + "> line juts to test " +  str(line))

	#print("-> the file is stored in memory")
	return lst

def write_res(lst):
	fd = open("res.txt", 'w')
	for i in lst:
		fd.write(str(int(i)))
		fd.write('\n')

def make_computation_of_all_module(lst):
	resLst = []
	for i in lst:
		modTest = Module(i)
		modTest.computeFuel()
		#print("la masse est de : ", i, " et le plein de carburant est de : ", modTest.getFuel())
		resLst.append(modTest.getFuel())
	#print(resLst)
	#print(len(lst))
	#print(len(resLst))
	return resLst
	

def sum_of_everything(lst):
	res = 0
	for i in lst:
		res += i
		#print("res provisoir = ", res)
	print("--> Sum of everything : ", res)

def main():
	print("In The Main function")
	modTwelve = Module(12)
	modFourteen = Module(14)
	modNineteenSixteenNie = Module(1969)
	modHundredThousandSevenFiveSix = Module(100756)
	
	fd = open_a_file("test.txt")
	lst = store_file_in_list(fd)

	res_lst = make_computation_of_all_module(lst)
	sum_of_everything(res_lst)
	#write_res(resLst)
	modTwelve.computeFuel()
	modFourteen.computeFuel()
	modNineteenSixteenNie.computeFuel()
	modHundredThousandSevenFiveSix.computeFuel()

	if modTwelve.getFuel() != 2:
		print("\033[93mERROR\033[0m : for 12 as mass we only need 2 of fuel unit !")
	else:
		print("\033[92mOK!\033[0m : for 12 it is 2 the test passed ;-p")

	if modFourteen.getFuel() != 2:
		print("\033[93mERROR\033[0m : for 14 as mass we only need 2 of fuel unit !")
	else:
		print("\033[92mOK!\033[0m : for 14 it is 2 the test passed ;-p")

	if modNineteenSixteenNie.getFuel() != 654:
		print("\033[93mERROR\033[0m : for 1969 as mass we only need 654 of fuel unit !")
	else:
		print("\033[92mOK!\033[0m : for 1969 it is 654 the test passed ;-p")

	if modHundredThousandSevenFiveSix.getFuel() != 33583:
		print("\033[93mERROR\033[0m : for 100756 as mass we only need 33583 of fuel unit !")
	else:
		print("\033[92mOK!\033[0m : for 100756 it is 33583 the test passed ;-p")

	test_computation(100756, 33583)
	
	# modTest = Module(119580)
	# modTest.computeFuel()
	# test_computation(119580, 39858, modTest.getFuel())

	test_computation(119580, 39858)
	test_computation(37789, 12594)
	test_computation(26751, 8915)
	test_computation(33745, 11246)

def test_computation(ms, resGoaled):
	modTest = Module(ms)
	modTest.computeFuel()
	resGiven = modTest.getFuel()
	if resGiven != resGoaled:
		print("\033[93mERROR\033[0m : for", ms, "as mass we only need :", resGoaled, "of fuel unit !\n------------------------>whereas you give : ", resGiven)
	else:
		print("\033[92mOK!\033[0m : for", ms, "it is", resGoaled, "the test passed ;-p")


main()