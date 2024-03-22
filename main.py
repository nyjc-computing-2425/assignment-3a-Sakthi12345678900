nric = input('Enter an NRIC number: ')

# Type your code below
prefixes = ('S', 'T', 'F', 'G')
if nric[0] in prefixes and nric[1:7].isdecimal and len(nric) == 9 and nric[-1].isalpha():
  print('NRIC format is valid.')
else:
  print('NRIC fromat is invalid.')
total_sum = (int(nric[1] * 2)
 + int(nric[2] * 7)
 + int(nric[3] * 6)
 + int(nric[4] * 5)
 + int(nric[5] * 4)
 + int(nric[6] * 3)
 + int(nric[7] * 2))
prefix0 = ('T','G')
if nric.startswith(prefix0):
  new_sum = (total_sum) + 4
else:
  new_sum = (total_sum) 
  check_digit = (new_sum % 11)
  prefix1 = ('S','T')
  prefix2 = ('F','G')
  if nric.startswith(prefix1):
    if check_digit == 0 and nric.endswith('J'):
      print('NRIC is valid.')
    elif check_digit == 1 and nric.endswith('Z'):
      print('NRIC is valid.')
    elif check_digit == 2 and nric.endswith('I'):
      print('NRIC is valid.')
    elif check_digit == 3 and nric.endswith('H'):
      print('NRIC is valid.')
    elif check_digit == 4 and nric.endswith('G'):
      print('NRIC is valid.')
    elif check_digit == 5 and nric.endswith('F'):
      print('NRIC is valid.')
    elif check_digit == 6 and nric.endswith('E'):
      print('NRIC is valid.')
    elif check_digit == 7 and nric.endswith('D'):
      print('NRIC is valid.')
    elif check_digit == 8 and nric.endswith('C'):
      print('NRIC is valid.')
    elif check_digit == 9 and nric.endswith('B'):
      print('NRIC is valid')
    elif check_digit == 10 and nric.endswith('A'):
      print('NRIC is valid.')
    else:
      print('NRIC is invalid.')
      if nric.startswith(prefix2):
        if check_digit == 0 and nric.endswith('X'):
          print('NRIC is valid.')
        elif check_digit == 1 and nric.endswith('W'):
          print('NRIC is valid.')
        elif check_digit == 2 and nric.endswith('U'):
          print('NRIC is valid.')
        elif check_digit == 3 and nric.endswith('T'):
          print('NRIC is valid.')
        elif check_digit == 4 and nric.endswith('R'):
          print('NRIC is valid.')
        elif check_digit == 5 and nric.endswith('Q'):
          print('NRIC is valid.')
        elif check_digit == 6 and nric.endswith('P'):
          print('NRIC is valid.')
        elif check_digit == 7 and nric.endswith('N'):
          print('NRIC is valid.')
        elif check_digit == 8 and nric.endswith('M'):
          print('NRIC is valid.')
        elif check_digit == 9 and nric.endswith('L'):
          print('NRIC is valid.')
        elif check_digit == 10 and nric.endswith('K'):
          print('NRIC is valid.')
        else:
          print('NRIC is invaild.')