n1=0
n2=1

while True:
    n = n1 + n2
    if n>1000:
        break

    # if n in range(100,1000):
    if 100 < n < 1000:
        if ((n%2) == 0):
            print(n)
    n1=n2
    n2=n
