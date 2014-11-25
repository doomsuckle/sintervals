#!/usr/env python
import scipy.stats


def clopper_pearson(x, n, alpha=0.1):
    ''' Calculate the Clopper-Pearson confidence
    with tail probability alpha
    for x successes on n trials.
    http://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval
    
    Takes a float for alpha for symmetric tails
    >>> clopper_pearson(8, 10, 1-0.99)
        (0.35179883369516324, 0.98914949062025948)

    Takes a tuple or list for asymmetric tails.
    >>> clopper_pearson(8, 10, (0, 0.1))
        (0.0, 0.94547138000232922)''' 

    def alpha_typecheck(x):
        return type(x) == type(float()) and x < 1

    if alpha_typecheck(alpha):
        alpha_lo = alpha/2.
        alpha_hi = alpha/2.
    elif type(alpha) in (type(tuple()), type(list())):
        if len(alpha) == 2:
            alpha_lo, alpha_hi = alpha
    else:
        raise ValueError('Value of alpha is invalid')

    lo = scipy.stats.beta.ppf(alpha_lo, x, n - x + 1)
    hi = scipy.stats.beta.ppf(1 - alpha_hi, x + 1, n - x)
    return lo, hi


if __name__ == '__main__':

    print clopper_pearson(8, 10, 1-0.99)
    print clopper_pearson(8, 10, 1-0.95)
    print clopper_pearson(8, 10, 1-0.9)
# 99% confidence interval:	0.35180 < p < 0.98915
# 95% confidence interval:	0.44390 < p < 0.97479
# 90% confidence interval:	0.49310 < p < 0.96323



