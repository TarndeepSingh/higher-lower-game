"""
Project: Higher or Lower Game
Description: A command-line game where players guess which account
has more social media followers.
"""

import random
from art import logo, vs
from game_data import data


def format_account(account):
    """Return a formatted string for account data."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def is_guess_correct(guess, a_followers, b_followers):
    """Return True if the user's guess is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def get_random_account(exclude_account=None):
    """Return a random account different from the excluded one."""
    account = random.choice(data)
    while account == exclude_account:
        account = random.choice(data)
    return account


def play_game():
    print(logo)
    score = 0
    game_running = True

    account_a = get_random_account()
    account_b = get_random_account(exclude_account=account_a)

    while game_running:
        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower().strip()

        if guess not in ("a", "b"):
            print("❌ Invalid choice. Please type 'A' or 'B'.")
            continue

        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        print("\n" * 20)
        print(logo)

        if is_guess_correct(guess, a_followers, b_followers):
            score += 1
            print(f"✅ You're right! Current score: {score}")

            # Move B to A, and get a new B
            account_a = account_b
            account_b = get_random_account(exclude_account=account_a)
        else:
            print(f"❌ Sorry, that's wrong.")
            print(f"🏁 Final score: {score}")
            game_running = False


# Start the game
play_game()
