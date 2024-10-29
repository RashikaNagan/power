def factorial(n):
    product = 1

    for i in range(1,n+1):
        product = product * i

    print(product)



def recurrence(n):
    if n==1:
        return n
    else:
        return n*recurrence(n-1)


def power(x, y):
    product = 1

    for i in range(y):
        product = product * x
        print(product)

power(3,4)