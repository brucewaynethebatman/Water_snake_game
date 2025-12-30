# Snake Water Gun Game 🐍💧🔫

A beginner-friendly Python command-line game inspired by the classic **Snake–Water–Gun** game (similar to Rock–Paper–Scissors).  
This project focuses on practicing Python fundamentals, logical thinking, and Git/GitHub workflow.

---

## 📌 What Is This Project?

This is a simple Python game where:
- The **user** chooses between Snake, Water, or Gun.
- The **computer** randomly selects one option.
- The program compares both choices and decides the winner based on predefined rules.

The game runs entirely in the terminal.

---

## 🎯 Why I Built This Project

I built this project to:
- Improve my Python logic-building skills
- Understand how conditional statements work in real scenarios
- Practice using dictionaries in Python
- Learn how randomness works using Python’s `random` module
- Get hands-on experience with Git and GitHub (commit, amend, push, README)

This project helped me move from writing basic syntax to implementing complete program logic.

---

## ⚙️ How the Game Works

### Game Rules
- **Snake drinks Water → Snake wins**
- **Water disables Gun → Water wins**
- **Gun kills Snake → Gun wins**
- **Same choice → Match Draw**

### Logic Behind the Game
- Each option is assigned a numeric value:
  - Snake → `1`
  - Water → `-1`
  - Gun → `0`
- The computer randomly selects one value.
- The user input is converted into its numeric equivalent.
- Conditional statements are used to determine the winner.

---

## 🧠 How I Implemented It

Key concepts used in this project:
- `random.choice()` for computer selection
- Dictionaries for mapping:
  - User input → numeric value
  - Numeric value → readable choice
- Conditional logic using `if`, `elif`, and `else`
- Input handling and formatted output

---

## ▶️ How to Run the Project

### Prerequisites
- Python 3 installed

Check Python version:
```bash
python --version
Run the game
bash
Copy code
python water_sanke_game.py
User Input Options
Key	Meaning
s	Snake
w	Water
g	Gun

📤 Example Output
yaml
Copy code
Enter your choice: g
Your choice: gun
Computer choose: water
You Won!
📚 What I Learned From This Project
Converting user input into usable logic

Importance of consistent data types

Practical use of dictionaries

Debugging logical errors step by step

Understanding Git commits and amend

Writing proper project documentation using README.md

🚀 Future Improvements
Add score tracking

Allow multiple rounds

Add replay option

Improve input validation

Convert it into a GUI or web-based game

🧑‍💻 Author
Lokesh Kumawat
Beginner Python Developer
Focused on logic building and problem solving

📄 License
This project is open-source and free to use for learning purposes.

yaml
Copy code

---