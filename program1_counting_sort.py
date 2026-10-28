"""
Experiment 6: Linear-Time Sorting
Program 1: Counting Sort
Aim: Sort non-negative integers by counting their frequencies.
"""

def counting_sort(a):
    if not a:
        return []
    counts = [0] * (max(a) + 1)
    for x in a:
        counts[x] += 1
    result = []
    for value, count in enumerate(counts):
        for _ in range(count):
            result.append(value)
    return result

print(counting_sort([4, 2, 2, 8, 3, 3, 1]))
