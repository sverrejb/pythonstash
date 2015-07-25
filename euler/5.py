import time
start = time.clock()
def div20(n):
	for i in range(11,21):
		if n%i != 0:
			return False
	return True
i = 20
while True:
	if (div20(i)):
		print i
		break
	i+=20
print time.clock() - start