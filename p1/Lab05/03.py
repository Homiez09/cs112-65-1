odd = 0
while True:
    n = int(input('Enter number: ')) 
    if n >= 0:
        if n % 2 != 0:
            odd += 1
    else:
        break;   
print(f'Received {odd} odd numbers')
    