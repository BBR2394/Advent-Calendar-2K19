# -*- coding: utf-8 -*-
# @Author: Baptiste
# @Date:   2019-12-01 22:18:06
# @Last Modified by:   Baptiste
# @Last Modified time: 2019-12-01 22:27:11

#!/usr/local/bin/python3

class Module:
	def __init__(self, ms):
		self.fuel = 0
		self.masse = ms

	def computeFurl(self):
		self.fuel = 0

def main():
	print("In The Main function")
	modTwelve = Module(12)
	modFourteen = Module(14)
	modNineteenSixteenNie = Module(1969)
	modHundredThousandSevenFiveSix = Module(100756)

	modTwelve.computeFuel()
	modFourteen.computeFuel()
	modNineteenSixteenNie.computeFuel()
	modHundredThousandSevenFiveSix.computeFurl()

	if modTwelve.getFuel != 2:
		print("ERROR : for 12 as mass we only need 2 of fuel unit !")
	if modFourteen.getFuel != 2:
		print("ERROR : for 14 as mass we only need 2 of fuel unit !")
	if modNineteenSixteenNie.getFuel != 654:
		print("ERROR : for 1969 as mass we only need 654 of fuel unit !")
	if modHundredThousandSevenFiveSix.getFuel != 33583:
		print("ERROR : for 100756 as mass we only need 33583 of fuel unit !")

main()