import numpy as np
import sys
from numpy.lib.arraysetops import isin
from helper import decryption, isInvertible
from helper import getInverse
from helper import encryption
from helper import getIOC
from helper import openFile
from helper import findKey
from helper import isValidK

if __name__=="__main__":
	cipherText = openFile(sys.argv[1])
	simpleText = openFile(sys.argv[2])
	completeCipherText = openFile(sys.argv[3])
	for k in range(2, 11):
		if(not isValidK(cipherText, completeCipherText, k)):
			continue
		ct = np.array(cipherText)
		nt = np.array(simpleText)
		i = 0
		while(i + k*k<=len(cipherText)):
			key = findKey(ct, nt, i, k)
			if(key is None):
				#key is None
				i+=1
				continue

			normalt = simpleText[i:]
			while(len(normalt)%k != 0):
				normalt.append(0)
			encrypt = encryption(key, normalt)
			if(encrypt[0:len(cipherText)-i] != cipherText[i:len(cipherText)]):
				i+=1
				continue
			datas = np.split(np.array(completeCipherText), len(completeCipherText)/k)
			ret = []
			for j in range(0, len(datas)):
				datas[j] = np.matrix(datas[j])
				final = decryption(key, datas[j])
				for K in range(0, len(final[:])):
					ret.append(final[K, 0])
			finalret = []
			for j in range(0, len(ret)):
				finalret.append(chr((int(ret[j]))+ord('A')))
			ioc = getIOC(finalret)
			print("IC : "+str(ioc))
			if(ioc >=0.05 and ioc <=0.08):
				print(k)
				f = open('key.txt', 'w')
				a, b = np.shape(key)
				f.write(str(k)+"\n")
				for J in range(a):
					for K in range(b):
						f.write(str(key[J, K])+" ")
					f.write("\n")
				f.close()
				exit(0)
			i+=1
	print("KEY NOT FOUND")