"""
Finding how many index triplets exist based on a conditions:
1. d[a] > d[b] > d[c]
2. d[a] + d[b] + d[c] <= t
"""


from itertools import combinations


def triplets(t, d):
    sets = 0
    for i in combinations(d, 3):
        if sum(i) <= t:
            sets += 1
    return sets

def triplets1(t, d):
    sets = [i for i in combinations(d, 3) if sum(i) <= t]
    return len(sets)

def triplets2(t, d):
    d = [i for i in d if i <= t]
    sets = [i for i in combinations(d, 3) if sum(i) <= t]
    return len(sets)