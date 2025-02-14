# -*- coding: utf-8 -*-
# @Author: Shine Wu
# @Date:   2025-02-14 16:44:40
# @Last Modified by:   Shine Wu
# @Last Modified time: 2025-02-14 19:39:44


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Inverse doesn't exist")
    else:
        # x might be negative, so we take it modulo m
        return x % m

# 快速取余法 fast to get modulus
def fast_power(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

# Given values
N=11*17
A = 29
phi_N=(11-1)*(17-1)
# Find B
B = mod_inverse(A, phi_N)
print(f"The value of N is: {N}")
print(f"The value of phi_N is: {phi_N}")
print(f"The value of B is: {B}")
mes1=97
print(f"The value of mes1 is: {mes1}")
Data =fast_power(mes1,A,N)
print(f"The value of Data is: {Data}")
mes=fast_power(Data, B, N)
print(f"The value of mes is: {mes}")