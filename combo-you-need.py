from random import *
halo1=input("saratay zhmara : ")
for o in range (100000):
    mrx = str(randint(0,9999999))
    halo =(choice(halo1)+mrx)
    print(halo +":"+ halo)