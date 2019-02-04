def len_check(x):
  length = len(str((x)))
  if (length == 15) or (length == 16):
    return True
  else:
    return False 

def is_valid(x):
  card = x
  num_list= list((str(card)))
  sum_odd = 0
  sum_even = 0
  even_count = 0
  odd_count = 0
  total_sum = 0
  length = 0
  for i in num_list:
    length += 1
  print(length)
  count = 0
  if length == 16:
    odd_count = 15
    even_count = 14

  if total_sum % 10 == 0:
    return True
  else:
    return False


def main():
  cc_num = int(input('Enter at 15 or 16-digit credit card number: '))

  if not len_check(cc_num):
    print('Not a 15 or 16-digit number')
  else:
    if not is_valid(cc_num):

      print('Invalid credit card number')
    else:
      print('valid card number')



main()

