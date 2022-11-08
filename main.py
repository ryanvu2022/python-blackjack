from art import logo
import random


def deal_card():
    """Deal a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Take a list of cards and returns the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_score(user, computer):
    """Compare user score and computer score to finish the game"""
    if user == computer:
        return "It's a draw 🙃"
    elif computer == 0:
        return "You lose. Opponent has Blackjack 😱"
    elif user == 0:
        return "You win with a Blackjack 😎"
    elif user > 21:
        return "You went over. You lose ☹️"
    elif computer > 21:
        return "Opponent went over. You win 🤓 "
    elif user > computer:
        return "You win 🤗"
    else:
        return "You lose 😤"


def play_game():
    """Play the game"""
    print(logo)
    global computer_score, user_score
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"   Your cards: {user_cards}, current scores: {user_score}")
        print(f"   Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"  Your final hand: {user_cards}, final score: {user_score}")
    print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
