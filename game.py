import random
import art

# Generally speaking, I would expect a separated game logic that does not require any specific interface of interaction
# like web based interface or stdin/stdout streams. I would encapsulate the game into a class and let developers
# write their own interfaces to interact with a player themeselves. In such approach, we do not limit the application
# to bare terminal game or bare online web game. We can even run several instances of the game separately if we want to

def calculate_winner(players_hand, dealers_hand):  # this is untestable, arguments are put, nothing is returned
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
    # this is untestable, arguments are put, nothing is returned
    # maybe we do not need to rely on console output in the scope of game mechanics
    print(f"Dealers cards are: {dealer_cards} \n Dealers overall score: {dealer_score}")
    print(f"Your cards are: {player_cards} \n your overall score: {player_score}")

def black_jack_win():
    # this is untestable, arguments are put, nothing is returned
    print("You Win!\n")
    print(art.logo)
