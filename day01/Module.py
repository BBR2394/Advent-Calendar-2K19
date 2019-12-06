# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2019-12-01 22:43:24
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-12-03 13:04:25

import math
from WireMod import * 

def calc_fuel_require(ms):
	intPart = math.modf(ms / 3)
	fl = int(intPart[1]) - 2
	return fl

class Module:
	def __init__(self, ms):
		self.fuel = 0
		self.masse = ms
		self.fuelForFuel = 0
		self.totalFuel = 0
		self.wm = WireMod()

	def computeFuelForFuel(self):
		rtr = calc_fuel_require(self.fuel)
		self.fuelForFuel = rtr
		#print("we need : ", self.fuelForFuel, " for the fuel : ", self.fuel)
		while rtr > 2:
			prevrtr = rtr
			rtr = calc_fuel_require(rtr)
			self.fuelForFuel = self.fuelForFuel + rtr
			#print("we need : ", rtr, " for the fuel : ", prevrtr, " and we have : ", self.fuelForFuel)

	def computeFuel(self):
		self.fuel = calc_fuel_require(self.masse)
		# self.computeFuelForFuel()
		self.totalFuel = self.fuel + self.fuelForFuel


	def getFuel(self):
		return self.totalFuel

	def initWireModule(self):
		self.wm.initPan()