import math
hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
buyAmt = int(input("Enter shopping amount: "))

if hours < 0 or hours > 20 or minutes < 0 or minutes > 59:
  print("Invalid time.")
else:
  total_hours = hours + math.ceil(minutes/60)
  i = 0
  total = 0
  if buyAmt > 3001 :
    print("No charge, thank you.")
  else:
    while i <= total_hours :
      if i >= 5: # Hours > 5
        total += 50
      elif i >= 3: # Hours 3-4
        if buyAmt < 300:
          total += 20
      i += 1    
    if total > 0 :
      print(f"Total amount due is {total} Baht, thank you.")
    else:
      print("No charge, thank you.")