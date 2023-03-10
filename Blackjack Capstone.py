import random, art, subprocess, platform


def clear():
    subprocess.Popen("cls" if platform.system() == "Windows" else "clear", shell=True)


# Define game_loop in global scope
game_loop = False


def game_init():
    play_game = input("Would you like to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game == 'y':
        # Return True if user wants to play, assign to global game_loop variable
        return True
    else:
        return False


# Define player_cards, computer_cards, and current_score in global scope
# current_score = 0
# computer_score = 0

def deal_cards():
    global player_cards, computer_cards, current_score
    global computers_first_card, computer_score, full_deck
    player_cards = []
    computer_cards = []
    full_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards.extend(random.choices(full_deck, k=2))
    computer_cards.extend(random.choices(full_deck, k=2))
    computers_first_card = computer_cards[0]
    current_score = sum(player_cards)


def computers_hand():
    computer_score = sum(computer_cards)
    while computer_score <= 16:
        computer_cards.extend(random.sample(full_deck, k=1))
        computer_score = sum(computer_cards)


def replace_eleven_with_one(array):
    for i in array:
        if array[i] == 11:
            array[i] = 1
            break


def who_won():
    computer_score = sum(computer_cards)
    if computer_score > 21 or computer_score < current_score:
        print(f"Computers final hand: {computer_cards}, final score {computer_score}")
        print('You win! 🙂 ')

    elif computer_score == current_score:
        print(f"Computers final hand: {computer_cards}, final score {computer_score}")
        print('It\'s a draw')

    else:
        print(f"Computers final hand: {computer_cards}, final score {computer_score}")
        print('You lose.')


# Define compare function in global scope
def compare():
    global current_score, computer_score
    hit = input("Type 'y' to hit, type 'n' to stay: ").lower()
    if hit == 'n':
        computer_score = sum(computer_cards)
        print(f"Computers Hand: {computer_cards}, Computers current score: {computer_score}")
        current_score = sum(player_cards)
        if computer_score <= 16:
            computers_hand()
            who_won()
        else:
            who_won()
    elif hit == 'y':
        player_cards.extend(random.sample(full_deck, k=1))
        current_score = sum(player_cards)
        if current_score > 21:
            print('You busted!')
        elif current_score == 21:
            print('Blackjack! You win')
        else:
            current_score = sum(player_cards)
            print(f"You cards: {player_cards}, current score: {current_score}")
            compare()


# Call game_init() to set initial value of game_loop
game_loop = game_init()

while game_loop:
    print(art.logo)
    deal_cards()
    print(f"Your cards: {player_cards}, current score: {current_score}")
    print(f"Computers first card: {computers_first_card}")

    if current_score == 21:
        who_won()
    else:
        # Prompt user for input and call compare function
        compare()

    # Clear screen and ask user if they want to play again
    game_loop = game_init()
