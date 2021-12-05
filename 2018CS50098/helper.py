import numpy as np

def encryption(key, content):
	n, n = np.shape(key)
	ret = []
	datas = np.split(np.array(content), len(content)/n)
	for i in range(0, len(datas)):
		datas[i] = np.matrix(datas[i])
		rett = np.matmul(key, np.transpose(datas[i]))
		a, b = np.shape(rett)
		for j in range(0, a):
			ret.append(rett[j, 0]%26)
	return ret

def modulo(det, m):
	for i in range(1, m):
		if(((det%m)*(i%m))%m == 1):
			return i
	return -1

def getInverse(mat):
	det = int(round(np.linalg.det(mat)))
	modDet = modulo(det, 26)
	ret = np.linalg.inv(mat)
	ret = np.multiply(ret, det)
	ret = np.multiply(ret, modDet)
	n = len(ret)
	for j in range(0, n):
			for K in range(0, n):
				ret[j, K] = int(round(ret[j, K]))%26
	return ret

def decryption(key, cipher):
	invK = getInverse(key)
	n = len(key)
	for i in range(0, n):
		for j in range(0, n):
			invK[i, j] = int(round(invK[i, j]))%26
	P = np.matmul(invK, np.transpose(cipher))
	a, b = np.shape(P)
	for i in range(0, a):
		P[i, 0] = round(P[i, 0]) % 26
	return P


def isInvertible(cm):
	det = np.linalg.det(cm)
	det = int(round(det))%26
	if(det == 0):
		return False
	elif(det%2 == 0 or det == 13):
		return False
	return True


def getIOC(arr):
	N = len(arr)
	if(N==1):
		return 0.0
	dict = {}
	for i in range(0, N):
		if arr[i] in dict:
			dict[arr[i]]+=1
		else:
			dict[arr[i]] = 1
	sum = 0.0
	for key, val in dict.items():
		sum += val*(val-1)
	return sum/(N*(N-1))

def openFile(name):
	f = open(name, 'r')
	file = f.read()
	ret = []
	for i in range(0, len(file)):
		ret.append(ord(file[i])-ord('A'))
	f.close()
	return ret

def findKey(ct, nt, i, k):
	c1 = ct[i:i+(k*k)]
	n1 = nt[i:i+(k*k)]
	c1 = np.split(c1, k)
	n1 = np.split(n1, k)
	cm = np.transpose(np.matrix(c1))
	nm = np.transpose(np.matrix(n1))
	if(not isInvertible(nm) or not isInvertible(cm)):
		#return None
		return
	invN = getInverse(nm)
	key = np.matmul(cm, invN)
	a, b = np.shape(key)
	for j in range(0, a):
		for K in range(0, b):
			key[j, K] = int(round(key[j, K]))%26
	return key


def isValidK(cipherText, completeCipherText, k):
	if(len(cipherText) < k*k):
		return False
	if(len(completeCipherText)%k != 0):
		return False
	return True


def openFile(name):
	f = open(name, 'r')
	file = f.read()
	ret = []
	for i in range(0, len(file)):
		ret.append(ord(file[i])-ord('A'))
	f.close()
	return ret

def getKeyFromFile(name):
	key = []
	f= open(name, 'r')
	line = f.readline()
	while (line):
		l = line.split()
		temp = []
		for i in range(0, len(l)):
			temp.append(int(l[i]))
		key.append(temp)
		line = f.readline()
	f.close()
	return key
	