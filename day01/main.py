# -*- coding: utf-8 -*-
# @Author: Baptiste
# @Date:   2019-12-01 22:18:06
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-12-09 15:29:27

#!/usr/local/bin/python3

import math
from Module import * 
from Intcode import *
from PasswordBreaker import *
from WireMod import *
import time

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
	line = fd.readline(';')
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

def test_intcode_computer(lst):
	computer = Intcode()
	#print("###> dans test du int code et la list est : ", lst)
	lstRes = computer.computeIntcode(lst)
	#print("###> et la liste est mainteannt : ", lst)
	return lstRes

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

	modHundredThousandSevenFiveSix.computeFuelForFuel()

	test_computation(100756, 33583)
	
	# modTest = Module(119580)
	# modTest.computeFuel()
	# test_computation(119580, 39858, modTest.getFuel())

	test_computation(119580, 39858)
	test_computation(37789, 12594)
	test_computation(26751, 8915)
	test_computation(33745, 11246)
	#test_intcode_computer([1,9,10,3,2,3,11,0,99,30,40,50])
	#test_intcode_computer([1,0,0,0,99])
	#test_intcode_computer([2,3,0,3,99])
	#test_intcode_computer([2,4,4,5,99,0])
	#test_intcode_computer([1,1,1,4,99,5,6,0,99])
	theList = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,19,5,23,1,23,6,27,2,9,27,31,1,5,31,35,1,35,10,39,1,39,10,43,2,43,9,47,1,6,47,51,2,51,6,55,1,5,55,59,2,59,10,63,1,9,63,67,1,9,67,71,2,71,6,75,1,5,75,79,1,5,79,83,1,9,83,87,2,87,10,91,2,10,91,95,1,95,9,99,2,99,9,103,2,10,103,107,2,9,107,111,1,111,5,115,1,115,2,119,1,119,6,0,99,2,0,14,0]
	size = len(theList)
	print("la liste est d'une taille : ", size, "et est :", theList)
	#test_intcode_computer()
	i = 0
	j = 0
	while j < 100:
		while i < 100:
			#print("i = ", i, " et j = ", j)
			#print(theList)
			resLst = test_intcode_computer(theList)
			#print("id the list = ", id(theList), "id lst : ", id(resLst))
			#print(resLst)
			#print(resLst[0])
			#if i > 3:
			#	resLst[0] = 19690720
			#	print("bis : ", resLst[0] )
			if resLst[0] == 19690720: 
				print("le resultat est trouvé")
				print(resLst[1], "  ", resLst[2])
				print(resLst)
				break
			else :
				i += 1
				theList[1] = i
			#time.sleep(1)

		j += 1
		theList[2] = j
		i = 0
		theList[1] = i


	#test_intcode_computer([1,12,2,0,99, ])

def test_computation(ms, resGoaled):
	modTest = Module(ms)
	modTest.computeFuel()
	resGiven = modTest.getFuel()
	if resGiven != resGoaled:
		print("\033[93mERROR\033[0m : for", ms, "as mass we only need :", resGoaled, "of fuel unit !\n------------------------>whereas you give : ", resGiven)
	else:
		print("\033[92mOK!\033[0m : for", ms, "it is", resGoaled, "the test passed ;-p")


def mainDeux():
	pb = PassBrkr("273025-767253")
	#pb = PassBrkr("123456-444444")
	pb.breakeIt()

def mainWireMod():
	print("dans le main wire mod")
	wm = WireMod()
	wm.initPan()

def mainCalcOrbit():
	print("dans main calc mainCalcOrbit")


# main()
#mainDeux()
mainWireMod()