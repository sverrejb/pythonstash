import time
start = time.time()

def is_pan(number):
	if ''.join(sorted(str(number))) == '123456789':
		return True

def prod_results(number):
	i = 0
	string = ""
	while len(string)<=9:
		i += 1
		string = string + str(number*i)
		if len(string) == 9 and is_pan(int(string)):
			return int(string)

ans = 0
for i in range (9999, 1, -1):
	tmp = prod_results(i)
	if tmp > ans:
		ans = tmp
		break
print 'Answer:',ans,', time:',time.time()-start,'seconds.'