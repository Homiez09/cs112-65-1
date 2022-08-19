target = int(input("Enter a target (4-digit integer): "))
guess = int(input("Enter your guess (4-digit integer): "))
positionCount = 0
digitCount = 0
ans = ""

if target == guess:
  print("Congratulations, you just mastered my mind!!")
else:
  # check position
  i = target
  j = guess
  while not i == 0:
    if i % 10 == j % 10:
      positionCount += 1
    i //= 10
    j //= 10

  # check digit
  i = target
  while not i == 0:
    j = guess
    while not j == 0:
      if i % 10 == j % 10:
        digitCount += 1
      j //= 10
    i //= 10

  if positionCount == 0:
    ans += "No positions correct, "
  elif positionCount == 1:
    ans += "One position correct, " 
  elif positionCount == 2:
    ans += "Two positions correct, "
  elif positionCount == 3:
    ans += "Three positions correct, " 
  digitCount -= positionCount
  if digitCount == 0:
    ans += "no digits correct"
  elif digitCount == 1:
    ans += "one digit correct"
  elif digitCount == 2:
    ans += "two digits correct"
  elif digitCount == 3:
    ans += "three digits correct"
  elif digitCount == 4:
    ans += "four digits correct"
print(ans)