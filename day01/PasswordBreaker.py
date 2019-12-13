# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2019-12-04 08:18:52
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-12-06 02:16:28

import math
import time

class PassBrkr:
	def __init__(self, passwd):
		self.passwd = passwd
		self.passwdOne = passwd[:6]
		self.passwdTwo = passwd[7:]
		self.lstPasswd = []

	def convertInList(self):
		tmp = []
		# for i in self.passwd:
		# 	if i == '-':
		# 		self.lstPasswd.append(tmp)
		# 		tmp = []
		# 	if i != '-':
		# 		print(" i = ", i)
		# 		tmp.append(i)
		#self.lstPasswd.append(tmp)

	def isCroissant(self, passwd):
		nbDigit = len(str(passwd))
		strPasswd = str(passwd)
		i = 0
		while i < nbDigit - 1:
			if strPasswd[i] > strPasswd[i+1]:
				return False
			i += 1
		return True

	#def isOnlyTwiceDigit(self, passwd):


	def isDoubleFollowDigit(self, passwd):
		strPasswd = str(passwd)
		i = 0
		while i < len(strPasswd) - 1:
			if strPasswd[i] == strPasswd[i+1]:
				self.isOnlyTwiceDigit(strPasswd[i])
				return True
			i += 1
		return False

	def countFromFirstToSecond(self):
		i = int(self.passwdOne)
		j = int(self.passwdTwo)
		count = 0
		while i < j:
			#and self.isDoubleFollowDigit(i):
			if self.isCroissant(i) :
				count += 1
			#print("le mdp i = ", i)
			#print("est ce croissant : ", self.isCroissant(i))
			#print("y a t il deux meme chiffre successif : ", self.isDoubleFollowDigit(i))
			#time.sleep(0.1)
			i += 1
		print("il y en a count = ", count)

	def breakeIt(self):
		print(" i am hoing to break the password ", self.passwd)
		#self.convertInList()
		print(" lst 1 = ", self.passwdOne, " lst2 = ", self.passwdTwo)
		self.countFromFirstToSecond()