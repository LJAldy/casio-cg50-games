import random

fulldeck = 4*['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
def fisher_yates_shuffle(deck):
    for i in range(len(deck) - 1, 0, -1):
        j = random.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]

shuffledeck = fulldeck.copy()
fisher_yates_shuffle(shuffledeck)

def get_card():
    global shuffledeck
    newcard = shuffledeck[0]
    shuffledeck.pop(0)
    return newcard

def calculate_score(cards):
    score = sum([11 if card == 'A' else 10 if card in ['K', 'Q', 'J'] else int(card) for card in cards])
    for card in cards:
        if card == 'A' and score > 21:
            score -= 10
    return score

def display_board(player_cards, dealer_cards, game_over=False):
    print("\n==== BLACKJACK ====")
    print("You: "+', '.join(str(x) for x in player_cards)+"\nVal: "+str(calculate_score(player_cards)))
    if game_over:
        print("Dlr: "+', '.join(str(x) for x in dealer_cards)+"\nVal: "+str(calculate_score(dealer_cards)))
    else:
        print("Dlr: "+', '.join(str(dealer_cards[x]) for x in range(0,2))+"\nVal: "+str(calculate_score(dealer_cards))+"\n")

def blackjack():
    player_cards = [get_card(), get_card()]
    dealer_cards = [get_card(), get_card()]
    is_game_over = False

    while not is_game_over:
        player_score = calculate_score(player_cards)
        player_shown_score = calculate_score(player_cards[0:2])
        dealer_score = calculate_score(dealer_cards)
        if player_score > 21:
            is_game_over = True
            continue
        display_board(player_cards, dealer_cards)

        # Ask the player if they want to draw another card
        draw_another = input("3 to draw: ")
        if "3" in draw_another:
            player_cards.append(get_card())
        else:
            is_game_over = True

    # Dealer draws cards
    while dealer_score < 17 or (dealer_score < player_shown_score and player_shown_score < 22):
        dealer_cards.append(get_card())
        dealer_score = calculate_score(dealer_cards)
    display_board(player_cards, dealer_cards, True)

    # Determine the winner
    if player_score == dealer_score:
        print("It's a draw.")
        input()
    elif player_score == 21:
        x=input("Blackjack!\nYou win! ")
    elif dealer_score == 21:
        x=input("Dealer Blackjacks.\nYou lose. ")
    elif player_score > 21:
        if dealer_score > 21:
            x=input("You both went over.\nIt's a draw.")
        else:
            x=input("You went over.\nYou lose. ")
    elif dealer_score > 21:
        x=input("Dealer went over.\nYou win! ")
    elif player_score > dealer_score:
        print("You win!")
        input()
    else:
        print("You lose.")
        input()

# Run the game
while True:
    blackjack()
    if len(shuffledeck) < 16:
        shuffledeck = fulldeck.copy()
        fisher_yates_shuffle(shuffledeck)
        print("\n\n\n\n\nDeck shuffled.")
        input()