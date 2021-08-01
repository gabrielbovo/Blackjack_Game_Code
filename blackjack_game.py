from random import choice


def blackjack():
    """ This function starts Blackjack game! Have Fun! (Play it in full console) """

    def SPACE():
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()

    logo = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """

    # Deck
    deck = [
        "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
        "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K",
    ]

    # Defining Dictionaries and Lists to use:
    player_one = {"play1_symbols": [], "play1_value": [], "play1_total": 0}
    player_two = {"play2_symbols": [], "play2_value": [], "play2_total": 0}
    play1_cards_values = []
    play2_cards_values = []
    play1_cards_symbols = []
    play2_cards_symbols = []

    # Defining variables to use:
    player_turn = 0  # Player 1 turn is equal 0, Player 2 turn is equal 1
    play1_total_of_cards = 0
    play2_total_of_cards = 0

    # Functions for both players
    def picking_symbol_cards():
        """ Pick up a new card and add it into playX_cards_symbols."""
        if player_turn == 0:
            play1_cards_symbols.append(choice(deck))
        else:
            play2_cards_symbols.append(choice(deck))

    def convert_card(card_to_convert):
        """ See a symbol card and add your value inside playX_cards_values."""
        if card_to_convert == "A":
            value_of_card = 11
        elif card_to_convert in ("J", "Q", "K"):
            value_of_card = 10
        else:
            value_of_card = card_to_convert

        if player_turn == 0:
            play1_cards_values.append(value_of_card)
        else:
            play2_cards_values.append(value_of_card)

    def counting_cards():
        """
            Return the summation value of playX_cards_values.
            It also confer the value of ACE.
        """
        if player_turn == 0:
            play1_sum = 0
            play1_sum = sum(play1_cards_values)
            if 11 in play1_cards_values and play1_sum > 21:
                play1_cards_values.remove(11)
                play1_cards_values.append(1)
                return sum(play1_cards_values)
            else:
                return sum(play1_cards_values)
        else:
            play2_sum = sum(play2_cards_values)
            if 11 in play2_cards_values and play2_sum > 21:
                play2_cards_values.remove(11)
                play2_cards_values.append(1)
                return sum(play2_cards_values)
            else:
                return sum(play2_cards_values)

    # GAME CODE
    game_star = True
    print(logo)
    print("Welcome to BlackJack Game!")
    print('Play it in Pycharm full console.')
    print()
    print('PLAYER 1 TURN')
    print()
    # Starting the Game:
    while True:
        # Giving 2 symbols cards and their respective values for both players:
        for i in range(4):
            if i < 2:
                picking_symbol_cards()
                if i == 1:
                    for card in play1_cards_symbols:
                        convert_card(card)
                        play1_total_of_cards = counting_cards()
            else:
                player_turn = 1
                picking_symbol_cards()
                if i == 3:
                    for card in play2_cards_symbols:
                        convert_card(card)
                        play2_total_of_cards = counting_cards()
        player_turn = 0

        # Displaying the first cards:
        print(f'Opponent cards: [{play2_cards_symbols[0]}, ?]')
        print(f'Player One cards: {play1_cards_symbols}')
        print(f'Player One Summation: {play1_total_of_cards}')

        # Seeing if there was an Blackjack at first
        if play1_total_of_cards == play2_total_of_cards == 21:
            print()
            print("PLAYER 1 BLACKJACK")
            print("PLAYER 2 BLACKJACK")
            print("IT'S A DRAW")
            break
        elif play1_total_of_cards == 21:
            print()
            print("PLAYER 1 BLACKJACK")

        # Player 1 Hit or Pass Choice
        while True:
            if play1_total_of_cards == 21:
                break
            print()
            hit = input('Type "y" to get another card. Type "n" to Pass: ').lower()
            while hit not in ('y', 'n'):
                print("You gave an invalid option. Try Again !")
                hit = input('Type "y" to get another card. Type "n" to Pass: ').lower()
            if hit == 'n':
                break
            else:
                picking_symbol_cards()
                play1_cards_values = []
                for card in play1_cards_symbols:
                    convert_card(card)
                    play1_total_of_cards = counting_cards()
                if play1_total_of_cards > 21:
                    break
                elif play1_total_of_cards == 21:
                    print()
                    print("PLAYER 1 BLACKJACK")
                    break
                print(f'Player One cards: {play1_cards_symbols}')
                print(f'Player One Summation: {play1_total_of_cards}')
                print(f'Opponent cards: [{play2_cards_symbols[0]}, ?]')

        # Player 2 Round
        SPACE()
        print('PLAYER 2 TURN')
        player_turn = 1

        # Displaying Player 2 Information's:
        print(f'Opponent cards: [{play1_cards_symbols[0]}{", ?" * (len(play1_cards_symbols) - 1)}]')
        print(f'Player Two cards: {play2_cards_symbols}')
        print(f'Player TWO Summation: {play2_total_of_cards}')

        # Verifying if player one got more than 21
        if play1_total_of_cards > 21:
            print()
            print("Bust !")
            print('PLAYER 2 WON!')
            break
        # Verifying if player two got a blackjack
        if play2_total_of_cards == 21:
            print()
            print("PLAYER 2 BLACKJACK")
            break

        # Player 2 Hit or Pass choice
        while True:
            hit = input('Type "y" to get another card. Type "n" to Pass: ').lower()
            while hit not in ('y', 'n'):
                print("You gave an invalid option. Try Again !")
                hit = input('Type "y" to get another card. Type "n" to Pass: ').lower()
            if hit == 'n':
                break
            else:
                picking_symbol_cards()
                play2_cards_values = []
                for card in play2_cards_symbols:
                    convert_card(card)
                    play2_total_of_cards = counting_cards()
                print(f'Opponent cards: [{play1_cards_symbols[0]}{", ?" * (len(play1_cards_symbols) - 1)}]')
                print(f'Player Two cards: {play2_cards_symbols}')
                print(f'Player Two Summation: {play2_total_of_cards}')
                # Verifying if player two busted
                if play2_total_of_cards > 21:
                    break
                # Verifying if player two got a blackjack
                elif play2_total_of_cards == 21:
                    print()
                    print("PLAYER 2 BLACKJACK")
                    break

        # Consult if Player 2 got more than 21
        if play2_total_of_cards > 21:
            print()
            print("Bust !")
            print('PLAYER 1 WON!')
            break

        # Comparing Results
        if play1_total_of_cards > play2_total_of_cards:
            print()
            print("PLAYER 1 WON !")
            break
        elif play1_total_of_cards == play2_total_of_cards:
            print()
            print("IT'S A DRAW !")
            break
        else:
            print()
            print("PLAYER 2 WON !")
            break
        # End of the Game Code

    # Printing Final Cards and Final Values:
    print()
    print(f'PLAYER 1:\n Cards : {play1_cards_symbols}  Total: {play1_total_of_cards}')
    print(f'PLAYER 2:\n Cards : {play2_cards_symbols}  Total: {play2_total_of_cards}')


# Starts the Game inside a while loop, so the user can choose if wants to continue playing or not.
# Do you want to keep playing or not?
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    blackjack()
    print()
