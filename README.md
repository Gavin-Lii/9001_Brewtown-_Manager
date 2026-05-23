# Brewtown Manager
## Project Description
Brewtown Cafe Simulator is a terminal-based cafe management game developed in Python for the COMP9001 Final Project. The player takes on the role of a trainee manager at Brewtown Cafe, a struggling local coffee shop facing long queues, falling profits, and unhappy customers. Over a simulated 3-month period, players make business decisions every fortnight, including adjusting menu prices, hiring or reducing staff, and setting marketing strategies.

The goal is to achieve a total profit of $6000 and maintain customer satisfaction above 8/10 to earn a full-time manager promotion from head office.

## How To Run
Open a terminal in this folder:

```
cd Final_Project
python main.py
```

Follow the on-screen prompts to enter your name and begin the simulation.

## How To Run Tests

```
python test_cafe.py
```

## Main Features
* Terminal UI with emoji elements, formatted reports, and typewriter-style narrative dialogue.
* 6 fortnights of gameplay, each with a full financial and operations report.
* Staff management: hire or fire baristas and servers to control queue time.
* Menu price adjustment: raise or lower prices to balance revenue and customer satisfaction.
* Marketing system: choose from 4 levels of marketing campaigns to boost sales.
* Dynamic satisfaction system: queue time and pricing both affect customer satisfaction, which in turn affects sales volume.
* 4 possible endings based on profit and satisfaction performance.
* Game result automatically saved to `result.txt` after each playthrough.

## Game Rules
Each fortnight, the player can:
* Hire or fire staff — more staff reduces queue time and improves satisfaction
* Adjust menu prices — raising prices increases revenue but reduces sales volume; prices more than $2 above original lower satisfaction
* Set a marketing level — higher levels bring more customers but cost more per fortnight

Win conditions:
* Total profit ≥ $6000
* Customer satisfaction ≥ 8/10 at the end of the final fortnight

## Advanced COMP9001 Concepts Used
This project uses several COMP9001 concepts:
* Variables and data types
* Conditionals
* Loops
* Lists and dictionaries
* Functions
* Classes and objects
* File input/output
* Testing
* Program structure across multiple files

The main advanced topics are:
1. **More Flow Control (Week 8)**: `try` and `except` handle non-numeric price input in `display_price_menu`. `break` and `continue` are used throughout action menus.
2. **File I/O (Week 9)**: game result is saved to `result.txt` after each playthrough using file write operations.
3. **Testing (Week 10)**: `test_cafe.py` checks core logic including profit calculation, price-sales relationship, and staff management rules.
   
The project also uses classes and objects through the `Cafe` class in `cafe.py`.

## File Structure
```
Final_Project/
├── main.py
├── cafe.py
├── menu_data.py
├── ui.py
├── test_cafe.py
└── result.txt
```

## Saved Result File
After each game, a result file is created at:
```
result.txt
```
The saved file includes:
* Manager name
* Final total profit
* Final customer satisfaction score

## Limitations
* All customer decisions are simulated based on fixed formulas — there is no randomness in sales or customer behaviour.
* Staff can only be hired or fired one at a time per action.
* Marketing level applies equally to all menu items.
