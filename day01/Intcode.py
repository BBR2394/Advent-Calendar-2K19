# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2019-12-02 17:07:56
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-12-02 18:18:16

import math
import time

class Intcode:
	def __init__(self):
		self.resLst = []

	def computeIntcode(self, lstGiven):
		i = 0
		lst = lstGiven[:]
		lstCode = [1, 2, 99]
		#print("++> la list int code est : ", lst)
		while i < len(lst):
			if lst[i] == 1:
				#print("pp> do 1")
				lst[lst[i+3]] = lst[lst[i+1]] + lst[lst[i+2]]
				i += 4
			elif lst[i] == 2:
				#print("pp> do 2")
				lst[lst[i+3]] = lst[lst[i+1]] * lst[lst[i+2]]
				i += 4
			elif lst[i] == 99:
				#print("STOP")
				return lst
			else:
				print("ERROR unknow code ", lst[i])
				print(lst[i+1])
				print(lst[lst[i+1]])
				print(lst[i+1+1])
				print(lst[lst[i+2]])
				time.sleep(10)
				print(lst)
				return lst
		return lst
