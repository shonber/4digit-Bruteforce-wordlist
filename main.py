
# Project made by Shon Berengard.
# 4 digit password wordlist.

fb = open("4digit-Bruteforce-wordlist.txt", "w")

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                fb.write(str(i)+str(j)+str(k)+str(l)+ '\n')