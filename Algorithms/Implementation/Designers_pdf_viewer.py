# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?h_r=internal-search

import string

s = string.ascii_lowercase

def func(arr,w):
    w = list(w)
    l = [arr[s.index(i)] for i in w]
    r = max(l) * len(l) * 1
    return r

arr = list(map(int,input().strip().split()))
word = input()
print(func(arr,word))