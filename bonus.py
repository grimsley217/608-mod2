#bonus.py

import statistics
values = [(*range(1,101)), 100, 100]
#used the *range function to include a continuous list
#of numbers without typing them in one at a time

#also included a couple of additional 100s so there
#would be at least one value with a count higher than 1

a=len(values)
b=sum(values)
c=statistics.mean(values)
d=statistics.median(values)
e=statistics.multimode(values)
#multimade is used in case there are multipled mode values

print(values)
print('The count is ' + str(a) + '.')
print('The sum is ' + str(b) + '.')
print('The mean is ' + str(c) + '.')
print('The median is ' + str(d) + '.')
print('The mode is ' + str(e) + '.')
