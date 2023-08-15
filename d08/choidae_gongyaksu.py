def largest_num(num):
    i       = 2
    largest = 1

    while num % i == 0:
        num     = num // i
        largest = i

    for i in range(3, num + 1, 2):
        while num % i == 0:
            num     = num // i
            largest = i
        if (num <= 1):
            break

    return largest

print(largest_num(600851475143))