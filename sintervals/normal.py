#!/usr/env python
from math import sqrt


def normal_error(n1, N):
    '''Get the normal approximation for the uncertainty
    for n1 accepts out of N trials'''
    def typecheck(x):
        if type(x) not in (type(float()), type(int())):
            raise TypeError('Type must be numeric')
    if n1 > N:
        raise ValueError('In reality, n1 must be <= N')

    p = n1*1./N
    err = sqrt(p * (1 - p) / N)
    return p, err


def normal_band(n1, N, nstdev=1.):
    '''Get the normal approximated confidence
    band going out nstdev standard deviations'''
    if not all(map(lambda x: type(x) in
               (type(float()), type(int())),
               [n1, N, nstdev])):
        raise TypeError('Inputs must be numeric')
    p, sigma = normal_error(n1, N)
    return max(0, p - nstdev * sigma), min(1, p + nstdev * sigma)


if __name__ == '__main__':
    print normal_band(6, 10, 3.)
