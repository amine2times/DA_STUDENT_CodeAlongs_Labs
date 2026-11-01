#!/usr/bin/env python3
"""Day 5 code-along: Recall & Practice. Run: python3 <file> or ./<file>"""


grid = [[1,2], [3,4], [5,6]]
total = 0
#print(grid)
for row in grid:
    for value in row:
        if value % 2 == 0:
            total += value
print(total)

def area(width, height):
    return width * height
print(area(3,4))

# ===== 1. Loop + Conditional + Function, Together =====
# Count how many scores pass a threshold of 70. Here the answer is 3.
print('----- 1. Loop + Conditional + Function, Together -----')
# TODO: define count_passing(scores, threshold)
def count_passing(scores, threshold):
    count = 0
    for val in scores:
        if val >= threshold:
            count += 1
    return count

# TODO: return how many scores are >= threshold

# TODO: call it with [55, 82, 91, 40, 76] and 70; print the result
numbers = [55, 82, 91, 40, 76]
threshold = 70
print(count_passing(numbers, threshold))

def count_long_shifts(hours):
    count = 0
    for h in hours:
        if h >= 4:
            count +=1
        return count

print(count_long_shifts([3,4,6,2,5]))