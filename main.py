# Brewtown Cafe Simulator
# COMP9001 Final Project
# Run this file to start the program

from cafe import Cafe
from ui import display_intro, display_welcome, display_report,display_action_menu, display_staff_menu,display_price_menu, display_marketing_menu, display_fortnight_transition, display_ending

# Opening title screen and backstory
display_intro()

# Get player name for personalised dialogue
while True:
    player_name = input("Mia: Hi! I'm Mia, one of the staff here at Brewtown Cafe. You must be the new trainee manager! We've been waiting for you...\n     What's your name? ").strip()
    if player_name != "":
        break
    print("Mia: I didn't catch that — could you tell me your name?\n")

# Mission briefing and win conditions
display_welcome(player_name)

# Keep asking until valid input
while True:
    join_choice = input("Mia: Are you ready to take the challenge? (yes/no): ").lower()

    if join_choice == "yes":
        print("\nMia: Great. Let me show you the current situation of the cafe first...\n")
        cafe = Cafe("Brewtown Cafe")

        # Main game loop: 6 fortnights = 3 months
        for round_number in range(1, 7):
            display_report(cafe, player_name, round_number)

            # Keep showing the action menu until the player decides to move on
            while True:
                choice = display_action_menu()

                if choice == "1":
                    print('Mia: "Staff management selected."')
                    display_staff_menu(cafe)

                elif choice == "2":
                    print('Mia: "Price adjustment selected."')
                    display_price_menu(cafe)

                elif choice == "3":
                    print('Mia: "Marketing plan selected."')
                    display_marketing_menu(cafe)

                elif choice == "4":
                    if round_number == 6:
                        print('Mia: "Alright, time to see how we did over these 3 months..."')
                    else:
                        print('Mia: "Alright, let\'s move to the next fortnight."')
                    break

                else:
                    print('Mia: "Hmm... I need a number from 1 to 4."')

            # Recalculate queue time, satisfaction, and total profit after changes
            cafe.process_fortnight()

            # Loading message for the first 6 rounds
            if round_number < 6:
                display_fortnight_transition(round_number)

        # Final result displaying
        display_ending(cafe, player_name)
        break

    elif join_choice == "no":
        print("\nMia: No worries. Brewtown Cafe will keep looking for help...")
        print("Challenge ended.")
        break

    else:
        print("\nMia: Hmm... I didn't quite catch that. Could you answer with yes or no?\n")

