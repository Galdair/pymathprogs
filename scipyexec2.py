# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:59:00 2017

@author: gabor
"""
import numpy as np
anarray = np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis]
print(anarray[1:6:4])
print(np.tile((6,2),(8,4)))
is_prime = np.ones((1000,), dtype=bool)
is_prime[:2] = 0
N_max = int(np.sqrt(len(is_prime)))
for j in range(2, N_max):
    is_prime[2*j::j] = False
print(is_prime)