def numberFactorial(num):
    for i in reversed(range(1, num + 1)):
        yield print(sumFactorial(i))

def sumFactorial(num):
    if (num == 1):
        return num

    return num * sumFactorial(num - 1)

factorial = numberFactorial(5)