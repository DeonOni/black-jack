import art
import random
import game

start = input("type \"s\" to start ").lower()

print(art.logo)

# those are all magic numbers, I have no clue what exactly those represent. Additionally, you did not have to
# hardcode all those sequences of digits this way, use python's generators
cards = [11,11,11,11, 2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5, 6,6,6,6, 7,7,7,7, 8,8,8,8, 9,9,9,9, 10,10,10,10, 10,10,10,10, 10,10,10,10, 10,10,10,10,]

# I see a problem here, once you call random.choice, you do not remove an element out of the cards list.
# I think you better generate a cards list once, shuffle it and access its last element by pop method
player_cards = [random.choice(cards), random.choice(cards)]
player_score = sum(player_cards)
dealer_cards = [random.choice(cards), random.choice(cards)]
dealer_score = sum(dealer_cards)

while start == "s":  # Do we really need to store it as a separate variable?
    # Do we even need to force player to press 's'?

    print(f"Your cards are: {player_cards} \n your overall score: {player_score}")

    if player_score == 21:
        game.black_jack_win()
        break

    print(f"dealers first card is: {dealer_cards[0]}")

    # You could use signle brackets ' instead of double to avoid putting \ symbol before " in the text
    draw_another_card = input("Draw additional card or pass: \n\"draw\" or \"pass\" ").lower()

    # We do not check if player provides any other input besides "draw" or "pass"
    if draw_another_card == "draw":
        additional_card = random.choice(cards)
        if player_score == 20 and additional_card == 11:
            player_cards.append(1)  # It does not really seem like we need to store any information about cards at all
            # we are only interested in the score.
            # If we really want to represent what cards a player currently owns, why don't we use user friendly names
            # instead of magic numbers?
            player_score += 1
        else:
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

