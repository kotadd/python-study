while True:
  try:
    age = int(input('what is your age? '))
    10/age
    raise ValueError('hey cut it out')
  except ValueError as err:
    print(f'please enter a number \n {err}')
    continue
  except ZeroDivisionError as err:
    print(f'please enter age higher than 0 \n {err}')
    break
  else:
    print('here is else !')
    break
  finally:
    print('ok, i am finally done')
  print('can you hear me?')

