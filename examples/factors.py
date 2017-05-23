# Stolen from 
#   http://arthurvause.blogspot.com/2015/01/factoring-numbers-in-python-and-c.html
# and refactored a bit to work with python3

from fractions import gcd
from operator import mul
import random
import itertools


MAXLOOKUP=1000000
MAXSMALLPRIME=300

# prime_or_factor[n]==0 indicates n is a prime,
# otherwise prime_or_factor[n] holds a prime factor of n
prime_or_factor=[0]*(MAXLOOKUP+1)
max_p = int(MAXLOOKUP**0.5)+1
prime_or_factor[4::2]=[2]*len(prime_or_factor[4::2])
prime_or_factor[9::6]=[3]*len(prime_or_factor[9::6])
p=5
while (p <= max_p):
  if prime_or_factor[p]==0:
    prime_or_factor[p*p::2*p]=[p]*len(prime_or_factor[p*p::2*p])
  if p%6==5:
    p+=2
  else:
    p+=4

smallprimes = [p for p in range(2,MAXSMALLPRIME) if prime_or_factor[p]==0]

def all_factors( x ):
  if type(x)==list:
    allf = [1]
    for p in set(x):
      e=x.count(p)
      le = len(allf)
      pn = 1
      for i in range(e):
        pn *= p
        allf.extend([a*pn for a in allf[0:le] ])        
    return allf

  elif type(x)==int or type(x)==long:
    return all_factors(factorise(x))

  
#-----------------------------------------------
#-----------------------------------------------

def factorise_trial_division(n):
  if n==1:
    return []

  factors=[]
  for p in (2,3):
    while n%p==0:
      factors.append(p)
      n //= p
  q=5
  while q*q <= n:
    for p in (q,q+2):
      while n%p==0:
        factors.append(p)
        n //= p
    q+=6
  if n>1:
    factors.append(n)
  return factors  
#-----------------------------------------------
def factorise_lookup(n):
  i = prime_or_factor[n]
  f=[]  
  while i :
    f.append(i)
    n//=i
    i = prime_or_factor[n]
  if n>1:
    f.append(n)
  return f
#-----------------------------------------------

def brent(N,maxBrentTime=1.0):
  if N%2==0:
    return 2
  # http://xn--2-umb.com/09/12/brent-pollard-rho-factorisation suggests that
  #   m=1000 is the optimum value
  y,c,m = random.randint(1, N-1),random.randint(1, N-1), 200
  g,r,q = 1,1,1
  while g==1:             
    x = y
    for _ in range(r):
      y = (y*y+c)%N
    k = 0
    while (k<r and g==1):
      ys = y
      for _ in range(min(m,r-k)):
          y = (y*y+c)%N   
          q = q*(abs(x-y))%N
      g = gcd(q,N)
      k +=  m
    r = r*2

  if g==N:
    while True:
      ys = (ys*ys+c)%N
      g = gcd(abs(x-ys),N)
      if g>1:
        break
   
  return g  
#-----------------------------------------------

def millerRabin(n, factor=[1]):
  global factorFromMillerRabin 

  if n == 2: return True
  if n<2: return False
  if n%2==0:
    factor[0]=2  
    return False

  two64 = pow(2,64)
  if n < 2047: P=(2,)
  elif n < 1373653: P=(2,3)
  elif n < 9080191: P=(31,73)
  elif n < 4759123141: P=(2,7,61)
  elif n < 2152302898747: P=(2,3,5,7,11)
  elif n < 3474749660383: P=(2,3,5,7,11,13)
  elif n < 341550071728321: P=(2,3,5,7,11,13,17)
  elif n < 3825123056546413051: P=(2,3,5,7,11,13,17,19,23)
  elif n < two64: P=(2, 325, 9375, 28178, 450775, 9780504, 1795265022) #http://miller-rabin.appspot.com/
  else: P=[2,3,5,7,11,13,17,19,23]+[random.randint(24,n-2) for i in range(40)]

  if n < 3825123056546413051 and n in P: return True

  # find s,d so that d is odd and (2^s)d = n-1
  d = (n-1)>>1
  s = 1
  while d&1 == 0:
    d >>= 1
    s += 1

  for w in P:
    a = pow(w, d, n)
    if a == 1: continue
    r = 0
    while r < s:
      if a == n-1: break
      prev_a = a
      a = (a*a)%n
      if a==1:
        # Previous value of a was a square root of unity not equal to -1.
        # We can use this to find a factor of n
        factor[0]=gcd(prev_a - 1, n)
        return False
      r += 1
    if r == s:
      # If we arrive here, then a^(n-1) != 1 mod n,
      # so n cannot be a prime, but we can't find a factor of n
      factor[0]=1
      return False
  return True

#-----------------------------------------------

def factorise_large(n, maxBrentTime=1.0):
  brent_failures = 0
  brent_calls = 0 
  brent_avoid = 0

  if n <= MAXLOOKUP:
    return factorise_lookup(n)

  millerrabinfactor = [1]
  if millerRabin(n,millerrabinfactor):
    return [n]  

  if 1 < millerrabinfactor[0] < n : 
    p = millerrabinfactor[0] 
    brent_avoid+=1
  else:  
    p=brent(n, maxBrentTime)
    brent_calls+=1

  q=n//p
  if p>q:
    p,q = q,p
  if p==1:
    if millerRabin(q):  
      return [q]
    else:
      brent_failures+=1
      return factorise_large(q, maxBrentTime) # Try again (sometimes brent doesn't find factors)
  else:
    return factorise_large(p)+factorise_large(q)

#-----------------------------------------------
#  utility functions that a user can call
#-----------------------------------------------

def factorise(n, maxBrentTime=1.0):
  if n<=MAXLOOKUP:
    return factorise_lookup(n)

  factors=[]
  for p in smallprimes:
    while n%p==0:
      factors.append(p)
      n//=p
    
  if n ==1:
    return factors
  
  return factors + factorise_large(n, maxBrentTime)

def totient(n):
  f = factorise(n)
  t=1
  for x in set(f):
    t*=pow(x,f.count(x)-1)*(x-1)
  return t    

def unfactorise( d ):
  return reduce(mul, d, 1)

def radical( d ):
  if type(d)==list:  
    return reduce(mul, set(d), 1)
  else:
    return reduce(mul, set(factorise(d)), 1)
#-----------------------------------------------


if __name__=="__main__":
    f = factorise(2**42-1)
    print(f)

