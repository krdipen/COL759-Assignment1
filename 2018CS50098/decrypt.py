import numpy as np
import sys
from helper import decryption, isInvertible, getKeyFromFile
from helper import openFile

content = openFile(sys.argv[1])
mat = getKeyFromFile(sys.argv[2])

n = len(mat)
mat = np.matrix(mat)
if(len(content)%n != 0):
	print("Impossible, exiting")
	exit(0)

datas = np.split(np.array(content), len(content)/n)
ret = []
for i in range(0, len(datas)):
	datas[i] = np.matrix(datas[i])
	if(not isInvertible(mat)):
		print("Key not invertible, exiting")
		exit(0)
	final = decryption(mat, datas[i])
	for j in range(0, len(final[:])):
		ret.append(final[j, 0])

f = open(sys.argv[3], 'w')
for i in range(0, len(ret)):
	f.write(chr(int(ret[i])+ord('A')))
f.close()