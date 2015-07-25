import string
digs = string.digits + string.lowercase

def isPalindrome(s):
    return s == s[::-1]

def int2base(x, base):
  if x < 0: sign = -1
  elif x==0: return '0'
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return ''.join(digits)

ans = 0
for i in range(1,1000000):
  if (isPalindrome(str(i)) and isPalindrome(str(int2base(i, 8)))):
    ans += 1;
print ans