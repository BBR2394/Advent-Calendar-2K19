# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2019-12-01 22:43:24
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-12-01 23:51:44

import math

class Module:
	def __init__(self, ms):
		self.fuel = 0
		self.masse = ms

	def computeFuel(self):
		intPart = math.modf(self.masse / 3)
		self.fuel = int(intPart[1]) - 2

	def getFuel(self):
		return self.fuel