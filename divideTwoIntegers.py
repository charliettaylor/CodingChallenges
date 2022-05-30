# 29. Divide Two Integers

def divide(dividend: int, divisor: int) -> int:
    i = 0
    neg = False

    if dividend == 0:
        return 0
    if dividend == -2147483648 and divisor == -1:
        return 2147483647
    if dividend < 0:
        neg = not neg
    if divisor < 0:
        neg = not neg

    dividend, divisor = abs(dividend), abs(divisor)

    if divisor > dividend:
        return 0

    q = 0
    while dividend >= divisor:
        i = 0
        temp = divisor
        while dividend >= temp:
            temp = temp << 1
            i += 1
        dividend -= temp >> 1
        q += 1 << (i - 1)

    return max(-q, -pow(2, 31)) if neg else min(q, pow(2,31) - 1)

if __name__ == '__main__':
    print(divide(140, 18))