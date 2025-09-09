import random
import art

# Generally speaking, I would expect a separated game logic that does not require any specific interface of interaction
# like web based interface or stdin/stdout streams. I would encapsulate the game into a class and let developers
# write their own interfaces to interact with a player themeselves. In such approach, we do not limit the application
# to bare terminal game or bare online web game. We can even run several instances of the game separately if we want to

def calculate_winner(players_hand, dealers_hand):  # this is untestable, arguments are put, nothing is returned
    if players_hand > 21:
        return "YOU LOSE"
    elif dealers_hand > 21:
        return "YOU WIN"
    elif players_hand > dealers_hand:
        return "YOU WIN"
    elif players_hand < dealers_hand:
        return "YOU LOSE"
    else:
        return "IT\'S A TIE"

def dealer_draw(dealer_score, cards, dealer_cards):
    while dealer_score < 19:
        dealer_additional_card = next(iter(cards))
        dealer_additional_card_value = cards.pop(dealer_additional_card)
        dealer_cards.append(dealer_additional_card)
        dealer_score += dealer_additional_card_value
    return dealer_score

def print_score(dealer_cards, dealer_score, player_cards, player_score):
    # this is untestable, arguments are put, nothing is returned
    # maybe we do not need to rely on console output in the scope of game mechanics
    return f"Dealers cards are: {dealer_cards} \n Dealers overall score: {dealer_score}\n Your cards are: {player_cards} \n your overall score: {player_score}"

def black_jack_win():
    # this is untestable, arguments are put, nothing is returned
    # fixed
    return f"You Win!\n{art.logo}"

def deck_shuffle(cards):
    unshuffled_deck_list = list(cards.items())
    random.shuffle(unshuffled_deck_list)
    shuffled_deck = dict(unshuffled_deck_list)
    return shuffled_deck
