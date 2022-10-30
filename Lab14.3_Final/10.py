def scoreCal(card: str):
    list_card = card.split()
    count = 0
    higher = 0
    usage = []
    for i in range(len(list_card)):
        if count > 16:
            break
        usage.append(list_card[i])
        if list_card[i] == 'A':
            count += 1
        elif list_card[i] == 'J' or list_card[i] == 'Q' or list_card[i] == 'K':
            count += 10
            higher = 'K' if 'K' in usage else 'Q' if 'Q' in usage else 'J'
        else:
            if int(list_card[i]) > higher:
                higher = int(list_card[i])
            count += int(list_card[i])

    print(higher)
    return count if count <= 21 else 'busted'

print(scoreCal(input()))