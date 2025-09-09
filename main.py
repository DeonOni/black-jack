import art
import random
import game

start = input("type \"s\" to start ").lower()

print(art.logo)

# those are all magic numbers, I have no clue what exactly those represent. Additionally, you did not have to
# hardcode all those sequences of digits this way, use python's generators
cards = {"Ace of Spades":11,"Ace of Clubs":11,"Ace of Diamonds":11,"Ace of Hearts":11,
         "Spades 2":2,"Clubs 2":2,"Diamonds 2":2,"Hearts 2":2,
         "Spades 3":3,"Clubs 3":3,"Diamonds 3":3,"Hearts 3":3,
         "Spades 4":4,"Clubs 4":4,"Diamonds 4":4,"Hearts 4":4,
         "Spades 5":5,"Clubs 5":5,"Diamonds 5":5,"Hearts 5":5,
         "Spades 6":6,"Clubs 6":6,"Diamonds 6":6,"Hearts 6":6,
         "Spades 7":7,"Clubs 7":7,"Diamonds 7":7,"Hearts 7":7,
         "Spades 8":8,"Clubs 8":8,"Diamonds 8":8,"Hearts 8":8,
         "Spades 9":9,"Clubs 9":9,"Diamonds 9":9,"Hearts 9":9,
         "Spades 10":10,"Clubs 10":10,"Diamonds 10":10,"Hearts 10":10,
         "Jack of Spades":10,"Jack of Clubs":10,"Jack of Diamonds":10,"Jack of Hearts":10,
         "Queen of Spades":10,"Queen of Clubs":10,"Queen of Diamonds":10,"Queen of Hearts":10,
         "King of Spades":10,"King of Clubs":10,"King of Diamonds":10,"King of Hearts":10,}

shuffled_cards = game.deck_shuffle(cards)
# I see a problem here, once you call random.choice, you do not remove an element out of the cards list. -----> card removal feature will be added in future updates
# I think you better generate a cards list once, shuffle it and access its last element by pop method -----> list is generated once and at the moment never modified. To be honest i don't see the difference in approach of randomly choosing element from the list. Why should we change logic if result seems to be the same?
player_first_card = next(iter(shuffled_cards))
player_first_value = shuffled_cards.pop(player_first_card)
player_second_card = next(iter(shuffled_cards))
player_second_value = shuffled_cards.pop(player_second_card)
dealer_first_card = next(iter(shuffled_cards))
dealer_first_value = shuffled_cards.pop(dealer_first_card)
dealer_second_card = next(iter(shuffled_cards))
dealer_second_value = shuffled_cards.pop(dealer_second_card)

player_cards = [player_first_card, player_second_card]
player_score = player_first_value + player_second_value
dealer_cards = [dealer_first_card, dealer_second_card]
dealer_score = dealer_first_value + dealer_second_value

while start == "s":  # Do we really need to store it as a separate variable?
    # Do we even need to force player to press 's'? -----> to be honest not really but this is design choice, maybe it will be changed later

    print(f"Your cards are: {player_cards} \n your overall score: {player_score}")

    if player_score == 21:
        print(game.black_jack_win())
        break

    print(f"dealers first card is: {dealer_cards[0]}")

    # You could use signle brackets ' instead of double to avoid putting \ symbol before " in the text
    #fixed
    draw_another_card = input("Draw additional card or pass: 'draw' or 'pass' ").lower()

    # We do not check if player provides any other input besides "draw" or "pass"
    #fixed
    if draw_another_card == "draw":
        player_additional_card = next(iter(shuffled_cards))
        player_additional_card_value = shuffled_cards.pop(player_additional_card)
        if player_score == 20 and player_additional_card_value == 11:
            player_cards.append(player_additional_card)  # It does not really seem like we need to store any information about cards at all ----> we need to update player hand to properly show player which cards present in hand
            # we are only interested in the score. ----> When you play cards in real life you calculate the score in your head, but it does not mean we shouldn't show player his cards
            # If we really want to represent what cards a player currently owns, why don't we use user-friendly names -----> this feature is under development
            # instead of magic numbers?
            player_score += 1
        else:
            player_cards.append(player_additional_card)
            player_score += player_additional_card_value

        if player_score > 21:
            print(game.print_score(dealer_cards, dealer_score, player_cards, player_score))
            print(game.calculate_winner(player_score, dealer_score))
            break

    elif draw_another_card == "pass":
        dealer_score = game.dealer_draw(dealer_score, shuffled_cards, dealer_cards)
        print(game.print_score(dealer_cards, dealer_score, player_cards, player_score))
        print(game.calculate_winner(player_score, dealer_score))
        break
    else:
        print("Invalid input please try again ")
        continue

