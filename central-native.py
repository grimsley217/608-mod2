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
  z=y-1 #decrease the length by 1
  return (X[y//2]+X[z//2])/2
#[ ] searches the index, so since indexes start at 0, [number] looks at the 'number+1' value in the list
#if there are an odd number of elements, the indexes y//2 and z//2 are the same value, so dividing the sum by 2 returns the same middle value
#if there are an even number of elements, the middle indexes are y//2 and z//2 respectively, so dividing the sum by 2 returns the average of the two middle values

#creating function to help natively find the mode
def mode(example2):


print('The count is ' + str(a) + '.')
print('The sum is ' + str(b) + '.')
print('The mean is ' + str(c) + '.')
print('The median is ' + median(values) + '.')
print('The mode is ' + mode(values) + '.')
