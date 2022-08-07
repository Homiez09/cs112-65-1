<<<<<<< HEAD
tv = int(input('How many TVs? ')) * 6000
dvd = int(input('How many DVD players? ')) * 1500
audio = int(input('How many Audio Systems? ')) * 3000
totalPrice = tv + dvd + audio
discount = 0

print(f'Total price is {totalPrice:.2f} baht.')

if totalPrice >= 24000:
    discount = totalPrice * 0.2
    totalPrice = totalPrice - discount
    print(f"You've got a discount of {discount:.2f} baht.")

=======
tv = int(input('How many TVs? ')) * 6000
dvd = int(input('How many DVD players? ')) * 1500
audio = int(input('How many Audio Systems? ')) * 3000
totalPrice = tv + dvd + audio
discount = 0

print(f'Total price is {totalPrice:.2f} baht.')

if totalPrice >= 24000:
    discount = totalPrice * 0.2
    totalPrice = totalPrice - discount
    print(f"You've got a discount of {discount:.2f} baht.")

>>>>>>> 47493b7 (Update LAB05)
print(f'Your payment is {totalPrice:.2f} baht. Thank you!')