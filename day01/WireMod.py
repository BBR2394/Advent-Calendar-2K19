# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2019-12-03 13:01:27
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-12-06 05:42:14

import time

class WireMod:

	def __init__(self):
		self.wirePan = []

	def findSizeSquare(self, order):
		maxNbX = 0
		maxNbY = 0
		i = 1
		cpy = order[:]
		while len(cpy) > 0 :
			print("cpy est ", cpy)
			if cpy.find(',') != -1:
				num = int(cpy[1:cpy.find(',')])
			else :
				num = int(cpy[1:])
			print("num est : ", num)
			time.sleep(0.1)
			if cpy[0] == 'U' or cpy[0] == 'D':
				if num > maxNbX:
					maxNbX = num
					print("le max est ", maxNbX)
			if cpy[0] == 'L' or cpy[0] == 'R':
				if num > maxNbY:
					maxNbY = num
					print("le max est ", maxNbY)

			if cpy.find(',') != -1:
				cpy = cpy[cpy.find(',')+1:]
			else:
				cpy = ''
			if cpy == '':
				print("c'est vide")

		print("le max X est : ", maxNbX, "et le max nb Y : ", maxNbY)

	def initPan(self):
		# try:
		# 	fd = open(file_name, 'r')
		# 	print("-> The file is opened")
		# 	return fd
		# except  :
		# 	print("=> an error occured when opening the file")
		# 	return -1
		print("dans init pan du wire module")
		#self.findSizeSquare("R75,D30,R83,U83,U8,U3,L12,D49,R71,U7,L72,U111")
		self.findSizeSquare("U7,R6,D4,L4")