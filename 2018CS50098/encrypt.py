import numpy as np
import sys

from helper import encryption

f = open(sys.argv[1], 'r')
file = f.read()
content = []
for i in range(0, len(file)):
	if(file[i] >= 'A' and file[i] <='Z'):
		content.append(ord(file[i])-ord('A'))

mat = []
f.close()
f = open(sys.argv[2], 'r')
line = f.readline()
while(line):
	l = line.split()
	temp = []
	for i in range(0, len(l)):
		temp.append(int(l[i]))
	mat.append(temp)
	line = f.readline()
f.close()

n = len(mat)
mat = np.matrix(mat)
while(len(content)%n != 0):
	content.append(0)


encrypt = encryption(mat, content)

f = open(sys.argv[3], 'w')
for i in range(0, len(encrypt)):
	f.write(chr((int(encrypt[i]))+ord('A')))
f.close()
