from random import randint
import sys

answer = randint(int(sys.argv[1]),int(sys.argv[2]))
# generate a number 1~10
# input from user
# check that input is a number 1~10
while True:
  try:
    guess = int(input('guess a number 1~10: '))
    if 0 < guess < 11:
      if guess == answer:
        print('you are genious!')
        break
      elif guess < answer:
        print('the answer is larger than it!')
      else:
        print('the answer is less than it!')
  except ValueError as err:
    print(f'please enter a number: {err}')
