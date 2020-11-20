def faktorial(n):
    if n == 1:
        return n
    else:
        return (n * faktorial(n-1))

bilangan = int(input("input : "))
print(f"output : {faktorial(bilangan)}")