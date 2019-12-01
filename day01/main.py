# -*- coding: utf-8 -*-
# @Author: Baptiste
# @Date:   2019-12-01 22:18:06
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-12-01 22:43:35

#!/usr/local/bin/python3

import math
from Module import * 

def main():
	print("In The Main function")
	modTwelve = Module(12)
	modFourteen = Module(14)
	modNineteenSixteenNie = Module(1969)
	modHundredThousandSevenFiveSix = Module(100756)

	modTwelve.computeFuel()
	modFourteen.computeFuel()
	modNineteenSixteenNie.computeFuel()
	modHundredThousandSevenFiveSix.computeFuel()

	if modTwelve.getFuel() != 2:
		print("\033[93mERROR\033[0m : for 12 as mass we only need 2 of fuel unit !")
	else:
		print("\033[92mOK!\033[0m : for 12 it is 2, the test passed ;-p")

	if modFourteen.getFuel() != 2:
		print("\033[93mERROR\033[0m : for 14 as mass we only need 2 of fuel unit !")
	else:
		print("\033[92mOK!\033[0m : for 14 it is 2, the test passed ;-p")

	if modNineteenSixteenNie.getFuel() != 654:
		print("\033[93mERROR\033[0m : for 1969 as mass we only need 654 of fuel unit !")
	else:
		print("\033[92mOK!\033[0m : for 1969 it is 654, the test passed ;-p")

	if modHundredThousandSevenFiveSix.getFuel() != 33583:
		print("\033[93mERROR\033[0m : for 100756 as mass we only need 33583 of fuel unit !")
	else:
		print("\033[92mOK!\033[0m : for 100756 it is 33583, the test passed ;-p")


main()