def sum(numbers):
  total = 0
  for number in numbers:
    total += number
  return total

print(sum([5, 10, 15, 20]))

def recursive_sum(numbers):
  if not numbers:
    return 0
  print('Calling sum(%s)' % numbers[1:])
  remaining_sum = recursive_sum(numbers[1:])
  print('Call to sum(%s) returning %d + %d' % (numbers, numbers[0], remaining_sum))
  return numbers[0] + remaining_sum

print(recursive_sum([5, 10, 15, 20, 50]))