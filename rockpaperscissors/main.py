# rock paper scissors
import random

options = ("rock", "paper", "scissors")
print("Rock Paper Scissors: THE GAME")
player_name = input("What's your name? ")
play_mode_selector = input("Are you ready to play? (yes/no) ")
quitTrigger = False
player_score_count = 0
comp_score_count = 0

if play_mode_selector == "yes":
    print("Type 'quit' to quit the game any time.")
    while (not quitTrigger):
        randomize_option = random.choice(options)
        player_chosen = input("Rock, Paper, Scissors, shoot! (rock/paper/scissors) ")

        if randomize_option == "rock" and player_chosen.lower() == "rock":
            print(f"THE COMPUTER CHOSE: {randomize_option}")
            print("It's a tie!")
        elif randomize_option == "paper" and player_chosen.lower() == "paper":
            print(f"THE COMPUTER CHOSE: {randomize_option}")
            print("It's a tie!")
        elif randomize_option == "scissors" and player_chosen.lower() == "scissors":
            print(f"THE COMPUTER CHOSE: {randomize_option}")
            print("It's a tie!")

        # tie options - player winning

        elif randomize_option == "rock" and player_chosen.lower() == "paper":
            print(f"THE COMPUTER CHOSE: {randomize_option}")
            print(f"{player_name.upper()} WON!")
            player_score_count += 1
        elif randomize_option == "paper" and player_chosen.lower() == "scissors":
            print(f"THE COMPUTER CHOSE: {randomize_option}")
            print(f"{player_name.upper()} WON!")
            player_score_count += 1
        elif randomize_option == "scissors" and player_chosen.lower() == "rock":
            print(f"THE COMPUTER CHOSE: {randomize_option}")
            print(f"{player_name.upper()} WON!")
            player_score_count += 1

        # player winning - comp winning

        elif randomize_option == "rock" and player_chosen.lower() == "scissors":
            print(f"THE COMPUTER CHOSE: {randomize_option}")
            print("THE COMPUTER WON!")
            comp_score_count += 1
        elif randomize_option == "scissors" and player_chosen.lower() == "paper":
            print(f"THE COMPUTER CHOSE: {randomize_option}")
            print("THE COMPUTER WON!")
            comp_score_count += 1
        elif randomize_option == "paper" and player_chosen.lower() == "rock":
            print(f"THE COMPUTER CHOSE: {randomize_option}")
            print("THE COMPUTER WON!")
            comp_score_count += 1

        # terminating the game

        elif player_chosen.lower() == "quit":
            quitTrigger = True
            print("Exiting the game.")

        # incorrect input

        else:
            print("Incorrect input. Disregarding round.")

    # final scores
    print(f"Final scores: {player_name} has {player_score_count} points.")
    print(f"Final scores: COMPUTER has {comp_score_count} points.")
    if player_score_count == comp_score_count:
        print("It's a tie!")
    elif player_score_count > comp_score_count:
        print(f"{player_name} has won the game!")
    else:
        print(f"COMPUTER has won the game!")

elif play_mode_selector == "no":
    print("Terminating sequence.")
else:
    print("Incorrect input")