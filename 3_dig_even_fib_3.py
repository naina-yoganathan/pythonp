n1=0
n2=1

while True:
    n = n1 + n2
    if n>1000:
        break

 
    if (n > 100) and (n%2 == 0):
        print(n)
        
    n1=n2
    n2=n