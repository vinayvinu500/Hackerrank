# https://towardsdatascience.com/how-to-use-and-create-a-z-table-standard-normal-table-240e21f36e53
# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem
"""Lesson"""
# https://www.hackerrank.com/challenges/s10-normal-distribution-1/tutorial

import numpy as np
from scipy.integrate import quad 
from math import pi, sqrt, exp, erf


def z_score(x,mu,sd):
    # z-score 
    """
    z = (x - mu) / S.D
    """
    # x is the individual variable
    # mu is the mean of the distribution
    # sd is the standard deviation of the distribution
    return (x-mu)/ sd

def normalProbabilityDensityFunction(x):
    # z-table
    """
    probability density function : 
    f ( x | mean, S.D) = (1 / sqrt(2pi) ) ** ((-1/2)* ((x-mean)/s.d))**2)
    """
    # x is the z-score calculated
    return (1.0 / np.sqrt(2*np.pi)) * (np.exp((-x**2) / 2.0))

def pdf(x,m,s):
    # mean -> m, standard deviation -> s
    return (1.0 / (sqrt(2*pi)*s))* exp((-1/2)*((x-m)/s)**2)

def cdf(x,m,s):
    # f(x) = 1/2(1+erf((x-mean)/sd(sqrt(2))))
    # where erf(z) = 2/sqrt(pi)(integration:0->z(e^(-x**2)) dx)
    z = (x-m)/(s*sqrt(2))
    return (1+erf(z))/2
    
    
# print(quad(normalProbabilityDensityFunction,np.NINF,19.5)[0])


# let X be the random variable for normal distribution then probability density function will be 
# pmf => P(X=x) = (1.0/ sqrt(2*3.14)*sd)* (2.71828)**((-1/2)*(xi-mu)/sd)
# empirical rule says 
# 68% falls under one sd
# 95% falls under two sd
# 97.7% falls under three sd

def pdf(x,m,s):
    # mean -> m, standard deviation -> s
    return (1.0 / (sqrt(2*pi)*s))* exp((-1/2)*((x-m)/s)**2)
    
# Given that,    
mean = 20
SD =  2


# Q1. P(x<19.5) = ?
x = 19.5


# z-table lookup
q1, _ = quad(normalProbabilityDensityFunction, np.NINF, z_score(x,mean,SD))


# probability of the area under the 19 hours is
print(round(q1 * 100,3))

#================================================================#

# Q2. P(20 < x < 22) = P(x<22) - P(x<20)
x1 = 20
x2 = 22

# P(x<20) = ?
a1, _ = quad(normalProbabilityDensityFunction, np.NINF, z_score(x1,mean,SD))

# P(x<22) = ?
a2, _ = quad(normalProbabilityDensityFunction, np.NINF, z_score(x2,mean,SD))

# Probability of the area between 20 and 22
q2 = a2 - a1
print(round(q2*100, 3))
