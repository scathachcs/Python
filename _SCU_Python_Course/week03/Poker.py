while True :
    card=input("请输入缩写形式的扑克牌，例如：Enter the card notation: Q5 Queen of Spades，请输入：")
    valueFlag = True
    symbolFlag = True

    if card[0] in ['j','J']:
        value = 'Jack'
    elif card[0] in ['q','Q']:
        value = 'Queen'
    elif card[0] in ['k','K']:
        value = 'King'
    elif card[0] in ['a','A']:
        value = 'Ace'
    elif int(card[0]) in range(2,10,1):
        value = card[0]
    else:
        valueFlag = False

    if card[1] in ['h','H']:
        symbol = 'Heart'
    elif card[1] in ['s','S']:
        symbol = 'Spade'
    elif card[1] in ['c','C']:
        symbol ='Cube'
    elif card[1] in ['d','D']:
        symbol = 'Diamond'
    else:
        symbolFlag = False

    if len(card)==2 and valueFlag == True and symbolFlag == True :
        print(value + " of " + symbol)
    else:
        print("input error")

