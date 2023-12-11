import random

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [(card, suit) for suit in suits for card in cards]

def cardVal(card):
    if card[0] in ['Jack', 'Queen', 'King']:
        return 10
    elif card[0] == 'Ace':
        return 11
    else:
        return int(card[0])

random.shuffle(deck)

p_card = [deck.pop(), deck.pop()]
d_card = [deck.pop(), deck.pop()]

def BlackJack():
    while True:
        p_score = sum(cardVal(card) for card in p_card)
        d_score = sum(cardVal(card) for card in d_card)
        print("\n")
        print("Dealer cards: ", d_card)
        print("Dealer score: ", d_score)
        print('\n')
        print("Player cards: ", p_card)
        print("Player score: ", p_score)
       
        choice = input("What do you want to do? ['Hit' for another card 'Stand' to stop]")
        if choice.lower() == "hit":
            new_card = deck.pop()
            p_card.append(new_card)
            p_score += cardVal(new_card)
        elif choice.lower() == "stop":
            print("Dealer cards: ", d_card)
            print("Dealer score: ", d_score)
            print("\n")
            print("Player cards: ", p_card)
            print("Player score: ", p_score)
            break
        else:
            print("Invalid Entry dumb dumb")
            continue
        if p_score > 21:
            print("Dealer cards: ", d_card)
            print("Dealer score: ", d_score)
            print("\n")
            print("Player cards: ", p_card)
            print("Player score: ", p_score)
            print("Player Bust! Dealer Wins!")
            break
        
        while d_score <= 16:
            new_card = deck.pop()
            d_card.append(new_card)
            d_score += cardVal(new_card)

        print("Dealer cards: ", d_card)
        print("Dealer score: ", d_score)
        print("\n")

        if d_score > 21:
            print("Dealer cards: ", d_card)
            print("Dealer score: ", d_score)
            print("\n")
            print("Player cards: ", p_card)
            print("Player score: ", p_score)
            print("Dealer Bust! Player Wins!")
        elif p_score > d_score:
            print("Dealer cards: ", d_card)
            print("Dealer score: ", d_score)
            print("\n")
            print("Player cards: ", p_card)
            print("Player score: ", p_score)
            print("Player wins!")
        elif d_score > p_score:
            print("Dealer cards: ", d_card)
            print("Dealer score: ", d_score)
            print("\n")
            print("Player cards: ", p_card)
            print("Player score: ", p_score)
            print("Dealer Wins!")
        else:
            print("Dealer cards: ", d_card)
            print("Dealer score: ", d_score)
            print("\n")
            print("Player cards: ", p_card)
            print("Player score: ", p_score)
            print("Push!")

BlackJack()
