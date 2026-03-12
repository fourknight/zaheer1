for  n in range(1, 100):
    if n > 1:
        for j in range(2, n):
            if n % j == 0:
                break
            else:
               print(n,end=" ")
                