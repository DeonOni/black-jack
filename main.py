import art
import random
import game

start = input("type \"s\" to start ").lower()

print(art.logo)

cards = [11,11,11,11, 2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5, 6,6,6,6, 7,7,7,7, 8,8,8,8, 9,9,9,9, 10,10,10,10, 10,10,10,10, 10,10,10,10, 10,10,10,10,]
player_cards = [random.choice(cards), random.choice(cards)]
player_score = sum(player_cards)
dealer_cards = [random.choice(cards), random.choice(cards)]
dealer_score = sum(dealer_cards)

while start == "s":

    print(f"Your cards are: {player_cards} \n your overall score: {player_score}")

    if player_score == 21:
        game.black_jack_win()
        break

    print(f"dealers first card is: {dealer_cards[0]}")

    draw_another_card = input("Draw additional card or pass: \n\"draw\" or \"pass\" ").lower()

    if draw_another_card == "draw":
        additional_card = random.choice(cards)
        player_cards.append(additional_card)
        player_score += additional_card
        if player_score > 21:
            game.print_score(dealer_cards, dealer_score, player_cards, player_score)
            game.calculate_winner(player_score, dealer_score)
            break

    elif draw_another_card == "pass":
        dealer_score = game.dealer_draw(dealer_score, cards, dealer_cards)
        game.print_score(dealer_cards, dealer_score, player_cards, player_score)
        game.calculate_winner(player_score, dealer_score)
        break

