new_list = [1, 2, 3, 4, 5]
result = new_list[0]
print(result)
# index_error = new_list[5]
# print(index_error)

if 1 in new_list: print(True)

for n in new_list:
  if n == 1:
    print(True)

    break

"""
Insert = linear time/add to beginning of array, Appending = constant time/append to end of list

"""

numbers = []

numbers.append(2) 
numbers.extend([4,5,6])
print(numbers)