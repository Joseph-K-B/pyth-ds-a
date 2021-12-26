def merge_sort(list):
  """
  Sorts a list in ascending order
  Returns a new sorted list
  Divide: find midpoint and divide into sublists
  Conquer: Recursively sort sublists
  Combine: merge sorted sublists
  """

  if len(list) <= 1:
    return list
  
  """Divide"""
  left_half, right_half = split(list)

  """Conquer"""
  left = merge_sort(left_half)
  right = merge_sort(right_half)

  """Combine"""
  return merge(left, right)

def split(list):
  """
  Divide the unsorted list at midpoint into sublists
  Returns two sublists left/right
  """
  mid = len(list)//2
  left = list[:mid]
  right = list[mid:]

  return left, right

def merge(left, right):
  """
  Merges two lists/arrays sorting them in process
  Returns a new merged list
  """
  l = []
  i = 0
  j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      l.append(left[i])
      i += 1
    else:
      l.append(right[j])
      j += 1

  while i < len(left):
    l.append(left[i])
    i += 1

  while j < len(right):
    l.append(right[j])
    j += 1

  return l

def verify_sorted(list):
  n = len(list)

  if n == 0 or n == 1:
    return True

  return list[0] < list[1] and verify_sorted(list[1:])


alist = [54, 26, 93, 77, 40, 10]
l = merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))
print (merge_sort(alist))
