import random

def DealCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def distribute ():
    user_cards = []
    dealer_cards = []
    for _ in range(2):
        user_cards.append(DealCard())
        dealer_cards.append(DealCard())
    return user_cards
    return dealer_cards

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards)> 21 :
        cards.remove(11)
        cards.append(1)

    return (sum(cards))

def winner(user_score, dealer_score):
    if  user_score > 21:
        print("You went over 21. You lose!")
    elif dealer_score > 21:
        print("Dealer went over 21. You win!")
    elif user_score == dealer_score:
        print("It's a draw!")
    elif user_score == 0:
        print("Blackjack! You win!")
    elif dealer_score == 0:
        print("Dealer has a Blackjack! You lose!")
    elif user_score > dealer_score:
        print("You have a higher score. You win!")
    else:
        print("Dealer has a higher score. You lose!")
    #
    # if user_score == dealer_score:
    #     print("that a drow")
    # elif user_score > dealer_score and user_score < 21:
    #     print("you win")
    # elif dealer_score > user_score and dealer_score < 21:
    #     print("you lose")
    # elif user_score == 0 :
    #     print("you win")
    # elif dealer_score == 0 :
    #     print("you lose")



def dealer_hand(dealer_cards):
    while calc_score(dealer_cards) !=0 and calc_score(dealer_cards) < 17 :
        dealer_cards.append(DealCard())
    return dealer_cards

distribute ()

#user_cards,dealer_cards= distribute()
user_cards = distribute()
dealer_cards= distribute()

user_score= calc_score(user_cards)
dealer_score= calc_score(dealer_cards)



game_over = False

# print(user_cards)
# print(dealer_cards)







while not game_over:
    user_score = calc_score(user_cards)
    dealer_score = calc_score(dealer_cards)
    print(f"your cards are {user_cards} and your score is {user_score}")
    print(f"dealer first card is  {dealer_cards[0]} ")
    if user_score == 0 or dealer_score == 0 or user_score > 21 or dealer_score > 21:
        game_over = True
    else:
        more_card=input("would you like to drow anther card??")
        if more_card.upper() == 'Y':
            user_cards.append(DealCard())
            dealer_cards = dealer_hand(dealer_cards)

        else:
            game_over = True







print(f"your cards are {user_cards} and your score is {user_score}")
print(f"dealer cards are {dealer_cards} and his score is {dealer_score}")
winner(user_score, dealer_score)



