from time import sleep
from random import randint as rand

def ip_generator(n):
  l = []
  for i in range(n):
    a = rand(1,256)
    b = rand(1,256)
    c = rand(1,256)
    d = rand(1,256)
    s = str(a)+'.'+str(b)+"."+str(c)+"."+str(d)
    l.insert(i,s)
  
  return l
  
n = int(input("Numarul de ip = "))
k = ip_generator(n)

for i in range(n):
  print(k[i],"\n", end="\n")
  sleep(0.5)