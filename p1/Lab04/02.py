<<<<<<< HEAD
print('---<< Main Menu >>---')
print('{:>4s}{}'.format('', '<B>urger Meal'))
print('{:>4s}{}'.format('', '<C>hicken Meal'))
print('{:>4s}{}'.format('', '<P>asta Meal'))

m = input('Enter your choice: ')

if m == 'B' or m == 'b':
    print('---<< Burger Sub Menu >>---')
    print('{:>4s}{}'.format('', '<R>egular Burger'))
    print('{:>4s}{}'.format('', '<C>heese Burger'))
    print('{:>4s}{}'.format('', '<D>ouble Cheese Burger'))
    m = input('Enter your choice: ')
    if m == 'R' or m == 'r':
        print('Your Regular Burger is 60 Baht.')
    elif m == 'C' or m == 'c':
        print('Your Double Cheese is 75 Baht.')
    elif m == 'D' or m == 'd':
        print('Your Double Cheese Burger is 90 Baht.') 
    else:
        print('Invalid sub menu choice.')

elif m == 'C' or m == 'c':
    print('---<< Chicken Sub Menu >>---')
    print('{:>4s}{}'.format('', '<F>ried Chicken'))
    print('{:>4s}{}'.format('', '<G>rilled Chicken'))
    print('{:>4s}{}'.format('', "<C>hef's Chicken"))
    m = input('Enter your choice: ')
    if m == 'F' or m == 'f':
        print('Your Fried Chicken is 120 Baht.')
    elif m == 'G' or m == 'g':
        print('Your Grilled Chicken is 150 Baht.')
    elif m == 'C' or m == 'c':
        print("Your Chef's Chicken is 180 Baht.")
    else:
        print('Invalid sub menu choice.')

elif m == 'P' or m == 'p':
    print('---<< Pasta Sub Menu >>---')
    print('{:>4s}{}'.format('', '<S>paghetti de Italiano'))
    print('{:>4s}{}'.format('', '<L>asagna Supreme'))
    print('{:>4s}{}'.format('', '<M>acaroni Special'))
    m = input('Enter your choice: ')
    if m == 'S' or m == 's':
        print('Your Spaghetti de Italiano is 90 Baht.')
    elif m == 'L' or m == 'l':
        print('Your Lasagna Supreme is 120 Baht.')
    elif m == 'M' or m == 'm':
        print('Your Macaroni Special is 100 Baht.')
    else:
        print('Invalid sub menu choice.')

else:
=======
print('---<< Main Menu >>---')
print('{:>4s}{}'.format('', '<B>urger Meal'))
print('{:>4s}{}'.format('', '<C>hicken Meal'))
print('{:>4s}{}'.format('', '<P>asta Meal'))

m = input('Enter your choice: ')

if m == 'B' or m == 'b':
    print('---<< Burger Sub Menu >>---')
    print('{:>4s}{}'.format('', '<R>egular Burger'))
    print('{:>4s}{}'.format('', '<C>heese Burger'))
    print('{:>4s}{}'.format('', '<D>ouble Cheese Burger'))
    m = input('Enter your choice: ')
    if m == 'R' or m == 'r':
        print('Your Regular Burger is 60 Baht.')
    elif m == 'C' or m == 'c':
        print('Your Double Cheese is 75 Baht.')
    elif m == 'D' or m == 'd':
        print('Your Double Cheese Burger is 90 Baht.') 
    else:
        print('Invalid sub menu choice.')

elif m == 'C' or m == 'c':
    print('---<< Chicken Sub Menu >>---')
    print('{:>4s}{}'.format('', '<F>ried Chicken'))
    print('{:>4s}{}'.format('', '<G>rilled Chicken'))
    print('{:>4s}{}'.format('', "<C>hef's Chicken"))
    m = input('Enter your choice: ')
    if m == 'F' or m == 'f':
        print('Your Fried Chicken is 120 Baht.')
    elif m == 'G' or m == 'g':
        print('Your Grilled Chicken is 150 Baht.')
    elif m == 'C' or m == 'c':
        print("Your Chef's Chicken is 180 Baht.")
    else:
        print('Invalid sub menu choice.')

elif m == 'P' or m == 'p':
    print('---<< Pasta Sub Menu >>---')
    print('{:>4s}{}'.format('', '<S>paghetti de Italiano'))
    print('{:>4s}{}'.format('', '<L>asagna Supreme'))
    print('{:>4s}{}'.format('', '<M>acaroni Special'))
    m = input('Enter your choice: ')
    if m == 'S' or m == 's':
        print('Your Spaghetti de Italiano is 90 Baht.')
    elif m == 'L' or m == 'l':
        print('Your Lasagna Supreme is 120 Baht.')
    elif m == 'M' or m == 'm':
        print('Your Macaroni Special is 100 Baht.')
    else:
        print('Invalid sub menu choice.')

else:
>>>>>>> 47493b7 (Update LAB05)
    print('Invalid main menu choice.')