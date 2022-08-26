def fibonaccirecursivo(n):
    if n > 1:
        return fibonaccirecursivo(n-1) + fibonaccirecursivo(n-2)
    return n
for i in range(13):
    print(fibonaccirecursivo(i))
