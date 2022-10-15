ls = {}
while True:
    data = input()
    if data == "end":
        break
    data = data.split()
    user = data[0]
    price = int(data[1])

    if user not in ls:
        ls[user] = [price]
    else:
        ls[user] += [price]

winner = ['', 0]
for detail in sorted(ls):
    if max(ls[detail]) > winner[1]:
        winner = [detail, max(ls[detail])]
    if len(ls[detail]) ==  1:
        print(f"{detail} bid at the price of {max(ls[detail]):.1f} baht in {len(ls[detail])} time.")
    else:
        print(f"{detail} bid at the price of {max(ls[detail]):.1f} baht in {len(ls[detail])} times.")
print(f'The winner is {winner[0]}.')