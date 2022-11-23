def isPrime(number):
    for i in range (2,number):
        if number%i == 0:
            return False
    return True

bigNum = 600851475143

halfNum = bigNum // 2


lpf = 0
print(halfNum)
for i in range (halfNum,2,-2):
    print(i)
    if bigNum%i == 0:
        print(i, " is a factor")
        if isPrime(i):
            print(i, " is the largest prime factor")
            break


