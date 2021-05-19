#central-with-statistics.py
"""The following calculates count, sum, mean, median, and mode WITH the statistics module."""

import statistics
values = [47, 95, 88, 73, 88, 84]

a=len(values)
b=sum(values)
c=statistics.mean(values)
d=statistics.median(values)
e=statistics.mode(values)

print('The count is ' + str(a) + '.')
print('The sum is ' + str(b) + '.')
print('The mean is ' + str(c) + '.')
print('The median is ' + str(d) + '.')
print('The mode is ' + str(e) + '.')
