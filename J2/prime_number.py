# import data_structure
# from data_structure import range_step_float

def is_prime(n):
    if n ==1:
        return False
    sqrt_n = int(n ** (0.5))+1
    for i in range(2, n):
        if not n % i:
            return False

    return True

def all_prime_before(n):
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)

    return result

def sum_prime_before(n):
    all_prime = all_prime_before(n)
    sum = 0
    import pdb; pdb.set_trace()
    for i in all_prime:
        sum += i

    return sum


# print(sum_prime_before(3))

# print(range_step_float(1, 2, 0.1))


# def fibo(n):
#     if n < 3:
#         return 1

#     a , b = 1 , 1

#     for i in range(1, n):
#         a , b = b , a+b

#     return a



def fibo2(n):
    if n < 3:
        return 1

    return fibo2(n-1) + fibo2(n-2)




def fibo_seq(n):
    result = []
    for i in range(1, n+1):
        result.append(fibo(i))

    return result

print(fibo2(40))