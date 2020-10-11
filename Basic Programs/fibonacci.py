# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fastFib(n):
    result=[0,1]
    for i in range(2,n+1):
        result.append(result[i-1]+result[i-2])
    return result[n]


if __name__ == '__main__':
    n = int(input())
    print(fastFib(n))
