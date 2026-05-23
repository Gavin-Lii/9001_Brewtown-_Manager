import time
import random

def typewriter(text, delay=0.05):
    # Print text character by character for a narrative effect
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Game Title
def display_intro():
    print('''===================================
      ☕ BREWTOWN CAFE ☕
===================================''')
    typewriter("The cafe has been struggling recently...")
    time.sleep(0.5)
    typewriter("Long queues, unhappy customers, and falling profits.")
    print()

# Rules introduction
def display_welcome(player_name):
    typewriter(f"Mia: Nice to meet you, {player_name}!")
    time.sleep(0.5)
    typewriter("Mia: You are now being considered as the trainee manager of Brewtown Cafe.")
    print('''
🎯 Your Mission:
1. Manage the cafe for 3 months
2. Make decisions every 2 weeks
3. Achieve a total profit of $6000 and maintain customer satisfaction above 8/10

⭐ If you meet the target, head office will promote you to a full-time manager. ⭐
''')

# Display emoji for different satisfaction score
def get_satisfaction_emoji(score):
    if score >= 9:
        return "😊"
    elif score >= 7:
        return "🙂"
    elif score >= 5:
        return "😐"
    elif score >= 3:
        return "😠"
    else:
        return "😡"

# Full snapshot of the cafe's current state, shown at the start of each fortnight
def display_report(cafe, player_name, round_number):
    print("===================================")
    print("         BREWTOWN REPORT")
    print("===================================\n")
    time.sleep(0.5)

    print(f"Manager:                {player_name}")
    print(f"Fortnight:              {round_number}\n")
    time.sleep(0.5)

    print("👨‍🍳 STAFF")
    print(f"Baristas:               {cafe.baristas}")
    print(f"Servers:                {cafe.servers}\n")
    time.sleep(0.5)

    print("💰 FINANCE")
    print(f"Revenue:                ${cafe.calculate_revenue()}")
    print(f"Product Cost:           ${cafe.calculate_product_cost()}")
    print(f"Staff Cost:             ${cafe.calculate_staff_cost()}")
    print(f"Marketing Cost:         ${cafe.calculate_marketing_cost()}")
    print(f"Profit:                 ${cafe.calculate_profit()}")
    print(f"Total Profit:           ${cafe.total_profit}\n")
    time.sleep(0.5)

    print("⏳ OPERATIONS")
    print(f"Queue Time:             {cafe.queue_time} mins")
    emoji = get_satisfaction_emoji(cafe.satisifaction)
    print(f"Customer Satisfaction:  {emoji} {cafe.satisifaction}/10\n")
    time.sleep(0.5)

    print("☕ MENU")
    index = 0
    while index < len(cafe.menu):
        item = cafe.menu[index]
        sales = cafe.calculate_item_sales(item)
        print(f"{index + 1}. {item['name']:<20} ${item['price']}  ({sales} sold)")
        index+=1
    time.sleep(0.5)

# Action list
def display_action_menu():
    print('''
===================================
          MANAGER ACTIONS
===================================

What would you like to adjust this fortnight?

1. Hire or reduce staff
2. Change menu prices
3. Set marketing level
4. Continue to next fortnight
''')
    choice = input("Choose an action (1-4): ")
    return choice


# Each entry: (display name, cost string, effect description)
MARKETING_PLANS = {
    0: ("No marketing",         "$0/fortnight",    "No extra reach."),
    1: ("Flyers on the street", "$500/fortnight",  "Hand out leaflets near the cafe. +20 sales/item."),
    2: ("Bus stop posters",     "$1000/fortnight", "Posters across local bus stops. +40 sales/item."),
    3: ("Social media ads",     "$1500/fortnight", "Instagram & TikTok campaign. +60 sales/item."),
}

# Staff management
def display_staff_menu(cafe):
    while True:
        staff_cost = cafe.calculate_staff_cost()
        print("\n👨‍🍳 STAFF STATUS")
        print("─" * 42)
        print(f"  Baristas  : {cafe.baristas}  ($600/fortnight each)")
        print(f"  Servers   : {cafe.servers}  ($450/fortnight each)")
        print(f"  Staff Cost: ${staff_cost}/fortnight")
        print("─" * 42)
        print("  1. Hire a barista  (+$600/fortnight)")
        print("  2. Hire a server   (+$450/fortnight)")
        print("  3. Fire a barista")
        print("  4. Fire a server")
        print("  5. Back to main menu")
        print("  ⚠  Must keep at least 1 barista and 1 server")
        print("     More staff = shorter queue time = higher satisfaction.")

        choice = input("\nMia: What would you like to do? (1-5): ").strip()

        if choice == "1":
            cafe.hire_barista(1)
            print(f"\nMia: New barista hired! You now have {cafe.baristas} baristas.")

        elif choice == "2":
            cafe.hire_server(1)
            print(f"\nMia: New server hired! You now have {cafe.servers} servers.")

        elif choice == "3":
            if cafe.baristas <= 1:
                print("\nMia: You can't fire your last barista — the coffee won't make itself!")
            else:
                cafe.fire_barista(1)
                print(f"\nMia: Barista let go. You now have {cafe.baristas} baristas.")

        elif choice == "4":
            if cafe.servers <= 1:
                print("\nMia: You need at least one server on the floor!")
            else:
                cafe.fire_server(1)
                print(f"\nMia: Server let go. You now have {cafe.servers} servers.")

        elif choice == "5":
            break

        else:
            print("\nMia: Please enter a number from 1 to 5.")


# Shows price, cost, and margin for each item — margin updates live as prices change
def display_price_menu(cafe):
    while True:
        print("\n☕ MENU PRICES")
        print("─" * 52)
        print(f"  {'#':<4} {'Name':<20} {'Price':>6}  {'Cost':>5}  {'Margin':>7}")
        print("─" * 52)
        index = 0
        while index < len(cafe.menu):
            item = cafe.menu[index]
            margin = item["price"] - item["cost"]
            # Flag items where price is more than $2 above original — triggers satisfaction penalty
            flag = " ⚠" if item["price"] > item["base_price"] + 2 else ""
            print(
                f"  {index + 1:<4} {item['name']:<20} ${item['price']:>5.2f}  ${item['cost']:>4.2f}  ${margin:>5.2f}{flag}")
            index += 1
        print("─" * 52)
        print("  ⚠  Raising price will reduce sales volume.")
        print("     Prices more than $2 above the original will lower customer satisfaction.")
        print("  0. Back to main menu")

        raw = input("\nMia: Enter item number to change price (or 0 to go back): ").strip()

        if raw == "0":
            break

        # Validate input: must be a number and within the menu index range
        if not raw.isdigit() or not (1 <= int(raw) <= len(cafe.menu)):
            print("\nMia: That's not a valid item number.")
            continue

        # Convert to 0-based index for list access
        index = int(raw) - 1
        item = cafe.menu[index]

        try:
            new_price = float(input(f"Mia: Enter new price for {item['name']} (current: ${item['price']:.2f}): $"))
        except ValueError:
            # Catch non-numeric input like letters or symbols
            print("\nMia: Please enter a valid number.")
            continue

        # Warn the player if they're pricing below ingredient cost
        if new_price < item["cost"]:
            print(f"\nMia: That's below cost price (${item['cost']:.2f})! We'd be losing money on every sale.")
            confirm = input("     Are you sure? (yes/no): ").lower()
            if confirm != "yes":
                continue

        cafe.update_item_price(index, round(new_price, 2))
        print(f"\nMia: Got it — {item['name']} is now ${new_price:.2f}.")

# Increasing sales by setting marketing level
def display_marketing_menu(cafe):
    while True:
        current = cafe.marketing_level
        plan = MARKETING_PLANS[current]
        current_name = plan[0]
        current_cost = plan[1]

        print("\n📢 MARKETING PLAN")
        print("─" * 60)
        print(f"  Current: Level {current} — {current_name}  ({current_cost})")
        print("─" * 60)

        # Show all available plans, marking the one currently active
        for level in MARKETING_PLANS:
            plan = MARKETING_PLANS[level]
            name = plan[0]
            cost = plan[1]
            desc = plan[2]
            marker = " ◀ current" if level == current else ""
            print(f"  {level}. {name:<25} {cost}{marker}")
            print(f"     {desc}")
        print("─" * 60)
        print("  ⚠  More marketing = more customers. Make sure you have enough staff!")

        raw = input("\nMia: Choose a marketing level (0-3, or press Enter to cancel): ").strip()

        if raw == "":
            break

        # Validate input: must be a digit and a recognised level
        if not raw.isdigit() or int(raw) not in MARKETING_PLANS:
            print("\nMia: Please enter a number between 0 and 3.")
            continue

        new_level = int(raw)

        if new_level == current:
            print(f"\nMia: You're already on Level {current}. No change made.")
            break

        # Apply the new marketing level
        cafe.marketing_level = new_level
        plan = MARKETING_PLANS[new_level]
        name = plan[0]
        desc = plan[2]
        print(f"\nMia: Marketing updated to Level {new_level} — {name}.")
        print(f"     {desc}")
        break

# Default message for rendering fortnight
def display_fortnight_transition(round_number):
    MESSAGES = [
        "Two weeks pass...",
        "The cafe opens its doors again...",
        "Another fortnight goes by...",
        "Time flies when you're pulling espresso shots...",
        "The regulars are back...",
    ]

    print(f"\nMia: Alright, wrapping up fortnight {round_number}...")
    time.sleep(1)

    message = random.choice(MESSAGES)
    typewriter(message, delay=0.04)
    time.sleep(1.5)

# Result Display
def display_ending(cafe, player_name):
    profit_goal = 6000
    satisfaction_goal = 8

    profit_ok = cafe.total_profit >= profit_goal
    satisfaction_ok = cafe.satisifaction >= satisfaction_goal

    time.sleep(0.5)
    typewriter("===================================")
    typewriter("         FINAL ASSESSMENT")
    typewriter("===================================\n")
    time.sleep(0.3)

    typewriter(f"Manager:               {player_name}")
    typewriter(f"Final Total Profit:    ${cafe.total_profit}")
    typewriter(f"Final Satisfaction:    {cafe.satisifaction}/10\n")
    time.sleep(0.5)

    # Result for achieving profit and satisfaction
    if profit_ok and satisfaction_ok:
        typewriter("Mia: I can't believe it... you actually turned this place around.")
        time.sleep(0.4)
        typewriter("Mia: Head office called this morning. They want to offer you the full-time manager position.")
        time.sleep(0.4)
        typewriter("Mia: Brewtown Cafe is thriving. And it's because of you.")
        time.sleep(0.5)
        print("\n⭐ CONGRATULATIONS — YOU'VE BEEN PROMOTED! ⭐\n")

    # Result for achieving profit but not satisfaction
    elif profit_ok and not satisfaction_ok:
        typewriter("Mia: The numbers look decent, but... customers have been complaining.")
        time.sleep(0.4)
        typewriter("Mia: Head office said the satisfaction score isn't where it needs to be.")
        time.sleep(0.4)
        typewriter("Mia: They're keeping you on as trainee for another term. Don't give up.")
        time.sleep(0.5)
        print("\n📊 SO CLOSE — PROFIT ACHIEVED, BUT SATISFACTION FELL SHORT.\n")

    # Result for not achieving profit and satisfaction
    elif not profit_ok and satisfaction_ok:
        typewriter("Mia: Customers love the place — the reviews have been great.")
        time.sleep(0.4)
        typewriter("Mia: But head office needs the numbers to add up too.")
        time.sleep(0.4)
        typewriter("Mia: They've decided to hold off on the promotion for now.")
        time.sleep(0.5)
        print("\n💔 SO CLOSE — SATISFACTION ACHIEVED, BUT PROFIT FELL SHORT.\n")

    # Result for not achieving profit and not satisfaction
    else:
        typewriter("Mia: I'm sorry. I really thought you had it this time.")
        time.sleep(0.4)
        typewriter("Mia: Head office has decided to bring in someone else.")
        time.sleep(0.4)
        typewriter("Mia: But hey — every manager starts somewhere. Maybe next time.")
        time.sleep(0.5)
        print("\n☕ GAME OVER — BETTER LUCK NEXT TIME.\n")

    # Informing users the result has been saved
    save_result(player_name, cafe.total_profit, cafe.satisifaction)
    print("📄 Your result has been saved to result.txt")


# save game result in a file
def save_result(player_name, total_profit, satisfaction):
    with open("result.txt", "w") as f:
        f.write(f"Manager: {player_name}\n")
        f.write(f"Final Profit: ${total_profit}\n")
        f.write(f"Satisfaction: {satisfaction}/10\n")