# lattice paths = (a+b) over a. Binomialkoeffisienten. I oppgava er det altsa "40 take 20"
from fractions import Fraction
print int(reduce(lambda x,y : x*y, (Fraction(40-i, i+1) for i in range(20)), 1) )
