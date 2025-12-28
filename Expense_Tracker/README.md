 🎯 Expense Tracker

A simple Python-based expense tracker that helps you record, categorize, and summarize your daily expenses.  
Built with **Python** and stored in **CSV files** for easy debugging in VS Code and importing into Excel.

---

🚀 Features
- Add new expenses with name, amount, and category (🍔 Food, 🏠 Home, 💼 Work, 🎉 Fun, ✨ Misc).
- Save expenses to a CSV file (`expenses.csv`).
- Summarize expenses by category with totals and remaining budget.
- Calculate daily budget based on days left in the month.
- Emoji-friendly categories for fun and readability.
- Colored terminal output for highlights.

---

📂 Project Structure
1. `expense.py` → Defines the `Expense` class (attributes: `name`, `amount`, `category`).
2. `expensetracker.py` → Main script: handles input, saving, summarizing.
3. `expenses.csv` → Stores expense records in CSV format.
4. `README.md` → Documentation for the project.

---

⚙️ Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/suryaantarvedi/Python.git
   cd Python/Expense_Tracker
2. Run the program: python expensetracker.py
3. Follow the prompts to add expenses and view summaries.

🖥️ Sample Output

🎯 Running Expense Tracker!
Enter expense name: Pizza
Enter expense amount: 250
Select a category:
  1. 🍔 Food
  2. 🏠 Home
  3. 💼 Work
  4. 🎉 Fun
  5. ✨ Misc
Enter a category number [1 - 5]: 1

Expenses By Category 📈:

  🍔 Food: $250.00
  
💵 Total Spent: $250.00

✅ Budget Remaining: $1750.00

👉 Budget Per Day: $58.33
