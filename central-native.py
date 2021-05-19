#central-native.py
"""The following calculates count, sum, mean, median, and mode WITHOUT the statistics module."""

values = [47, 95, 88, 73, 88, 84]

a=len(values)
b=sum(values)
c=sum(values)/len(values)

#creating function to help natively find the median
def median(X):
  X=sorted(X) #sorts the list and re-saves the order
  y=len(X) #calculates the number of items in the list
  z=y-1 

#creating function to help natively find the mode
def mode(example2):


print('The count is ' + str(a) + '.')
print('The sum is ' + str(b) + '.')
print('The mean is ' + str(c) + '.')
print('The median is ' + median(values) + '.')
print('The mode is ' + mode(values) + '.')
