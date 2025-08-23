import random
import art

def calculate_winner(players_hand, dealers_hand):
    if players_hand > 21:
        print("YOU LOSE")
    elif dealers_hand > 21:
        print("YOU WIN")
    elif players_hand > dealers_hand:
        print("YOU WIN")
    elif players_hand < dealers_hand:
        print("YOU LOSE")
    else:
        print("IT\'S A TIE")

def dealer_draw(dealer_score, cards, dealer_cards):
    while dealer_score < 19:
        additional_card = random.choice(cards)
        dealer_cards.append(additional_card)
        dealer_score += additional_card
    return dealer_score

def print_score(dealer_cards, dealer_score, player_cards, player_score):
    print(f"Dealers cards are: {dealer_cards} \n Dealers overall score: {dealer_score}")
    print(f"Your cards are: {player_cards} \n your overall score: {player_score}")

def black_jack_win():
    print("You Win!\n")
    print(art.logo)
