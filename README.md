# Personal Expense Tracker 💰

A simple personal expense tracker built with **Python and PostgreSQL**.
I built this project step by step to learn how Python applications work with databases, how to analyze stored data, and how to add basic security and AI-style features.

## 🚀 What can it do?

* Add, view, update, and delete expenses
* Search for specific expenses
* Calculate spending summaries
* Analyze spending by category
* Track spending by payment method
* Show daily and monthly spending
* Find recurring expenses
* Detect small expenses and possible money leaks
* Identify spending patterns
* Generate rule-based financial warnings
* Enter expenses using simple natural language
* Ask basic questions about spending using natural language
* Generate spending insights and suggestions
* Store data permanently using PostgreSQL
* Validate user input
* Protect against basic SQL injection
* Handle database errors
* Keep database credentials outside the source code
* Run basic automated database tests

## 🛠️ Technologies Used

* **Python**
* **PostgreSQL**
* **psycopg2**
* **python-dotenv**
* **pytest**
* **Git & GitHub**

## 📁 Project Structure

```text
personal-expense-tracker/
│
├── main.py
├── add_expense.py
├── view_expenses.py
├── update_expense.py
├── delete_expense.py
├── search_expense.py
├── expense_summary.py
│
├── category_summary.py
├── payment_summary.py
├── daily_summary.py
├── monthly_summary.py
├── category_percentage.py
├── top_categories.py
│
├── phase 7/
│   ├── smart_category.py
│   ├── natural_expense.py
│   ├── natural_query.py
│   ├── ai_spending_analysis.py
│   ├── smart_warnings.py
│   ├── monthly_ai_report.py
│   ├── personalized_suggestions.py
│   └── expense_assistant.py
│
├── phase 8/
│   ├── input_validation.py
│   ├── database_error_handling.py
│   ├── sql_injection_protection.py
│   ├── secure_connection.py
│   └── test_database.py
│
├── database.sql
├── .gitignore
└── README.md
```

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/nickdrx01/personal-expense-tracker.git
cd personal-expense-tracker
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

For Windows:

```bash
.venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install psycopg2-binary python-dotenv pytest
```

### 4. Set up PostgreSQL

Create a PostgreSQL database named:

```text
expense_tracker
```

Then create a `.env` file in the project folder:

```text
DB_HOST=localhost
DB_NAME=expense_tracker
DB_USER=postgres
DB_PASSWORD=YOUR_POSTGRES_PASSWORD
DB_PORT=5432
```

Replace `YOUR_POSTGRES_PASSWORD` with your local PostgreSQL password.

> **Important:** Never upload the `.env` file to GitHub.

### 5. Create the expenses table

Run:

```bash
python create_table.py
```

### 6. Start the application

```bash
python main.py
```

## 🔐 Security

While building the project, I also focused on some basic security practices:

* Parameterized SQL queries
* User input validation
* Database error handling
* Database credentials stored in environment variables
* `.env` excluded using `.gitignore`
* Basic SQL injection protection
* Automated database tests

## 🧪 Testing

The project includes basic tests using **pytest**.

Run:

```bash
pytest
```

The current tests check:

* PostgreSQL database connection
* Existence of the `expenses` table

## 📚 How I Built It

The project was developed in different stages instead of building everything at once:

1. Python fundamentals
2. PostgreSQL setup
3. Connecting Python with PostgreSQL
4. CRUD operations and search
5. Spending analytics
6. Spending pattern detection
7. AI-style features
8. Testing and security
9. Git and GitHub

This approach helped me understand each part before moving to the next one.

## 🔮 Future Improvements

Some things I would like to add later:

* Web-based interface
* Interactive spending dashboard
* Better natural-language processing
* Machine-learning based spending prediction
* Budget management
* Expense forecasting
* User authentication
* Support for multiple users

## 👨‍💻 About

**Nikhil Gawade**

B.Tech Computer Science Engineering Student

Interested in **Cybersecurity, Cloud Computing, Python, and Backend Development**.
