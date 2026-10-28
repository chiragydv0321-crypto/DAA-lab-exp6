"""
Experiment 6: Linear-Time Sorting
Program 4: Minimize Array Sum after K Operations
Aim: Repeatedly replace the largest value by its ceiling half.
"""

def minimize_sum(a, k):
    a = a[:]
    for _ in range(k):
        idx = 0
        for i in range(1, len(a)):
            if a[i] > a[idx]:
                idx = i
        a[idx] = (a[idx] + 1) // 2
    return sum(a)

print(minimize_sum([10, 20, 7], 4))
