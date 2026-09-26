# Personal Expense Tracker 💰

A personal expense tracker built with **Python and PostgreSQL**.

I built this project step by step to improve my understanding of Python, SQL, databases, data analysis, security, testing, and Git/GitHub. The idea was to start with a simple expense tracker and gradually add more useful features.

## 🚀 Features

### Expense Management

* Add expenses
* View expenses
* Update expenses
* Delete expenses
* Search expenses
* View spending summaries

### 📊 Spending Analysis

* Category-wise spending
* Payment-method analysis
* Daily spending
* Monthly spending
* Category percentage analysis
* Top spending categories
* Highest and lowest expenses
* Spending insights

### 🔍 Spending Patterns

* Find recurring expenses
* Detect small expenses
* Identify spending increases
* Find high-spending days
* Track category trends
* Analyze payment patterns
* Detect possible money leaks
* Generate rule-based insights

### 🤖 Smart Features

I also added some simple AI-style features to make the project more useful.

* Smart category suggestions
* Natural-language expense input
* Natural-language spending queries
* Spending analysis
* Smart warnings
* Monthly reports
* Personalized suggestions
* Expense assistant

> **Note:** These features are currently based on Python logic, keywords, and SQL queries. They do not use a machine-learning model or external LLM API yet.

### 🔐 Security & Testing

* User input validation
* Database error handling
* Parameterized SQL queries
* Basic SQL injection protection
* Database credentials stored in `.env`
* `.env` protected using `.gitignore`
* Automated database tests using `pytest`

## 🛠️ Technologies

* Python
* PostgreSQL
* psycopg2
* python-dotenv
* pytest
* Git
* GitHub

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
├── create_table.py
├── insert_sample_data.py
├── database.sql
├── requirements.txt
│
├── features/
│   ├── ai/
│   │   ├── smart_category.py
│   │   ├── natural_expense.py
│   │   ├── natural_query.py
│   │   ├── ai_spending_analysis.py
│   │   ├── smart_warnings.py
│   │   ├── monthly_ai_report.py
│   │   ├── personalized_suggestions.py
│   │   └── expense_assistant.py
│   │
│   ├── analytics/
│   │   ├── category_summary.py
│   │   ├── payment_summary.py
│   │   ├── daily_summary.py
│   │   ├── monthly_summary.py
│   │   ├── category_percentage.py
│   │   ├── top_categories.py
│   │   ├── expense_summary.py
│   │   ├── high_low_expense.py
│   │   └── spending_insights.py
│   │
│   ├── patterns/
│   │   ├── category_trends.py
│   │   ├── high_spending_days.py
│   │   ├── money_leak.py
│   │   ├── payment_patterns.py
│   │   ├── recurring_expenses.py
│   │   ├── rule_based_insights.py
│   │   ├── small_expenses.py
│   │   └── spending_increase.py
│   │
│   └── security/
│       ├── input_validation.py
│       ├── database_error_handling.py
│       ├── secure_connection.py
│       └── sql_injection_protection.py
│
├── tests/
│   └── test_database.py
│
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

```powershell
.venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL

Create a PostgreSQL database named:

```text
expense_tracker
```

Create a `.env` file in the project folder:

```text
DB_HOST=localhost
DB_NAME=expense_tracker
DB_USER=postgres
DB_PASSWORD=YOUR_POSTGRES_PASSWORD
DB_PORT=5432
```

Replace `YOUR_POSTGRES_PASSWORD` with your local PostgreSQL password.

> **Important:** Never upload the `.env` file to GitHub.

### 5. Create the database table

```bash
python create_table.py
```

### 6. Run the application

```bash
python main.py
```

## 🧪 Testing

The project uses **pytest** for basic automated testing.

Run:

```bash
pytest
```

Current test result:

```text
2 passed
```

The tests currently check:

* PostgreSQL database connection
* `expenses` table existence

## 🔒 Security

Security was also considered while building the project.

The application uses:

* Parameterized SQL queries
* Input validation
* Database error handling
* Environment variables for credentials
* `.gitignore` to protect `.env`
* Basic SQL injection protection

Real database passwords and other secrets should never be committed to GitHub.

## 📚 Development Journey

I built the project gradually instead of trying to create everything at once.

1. Python fundamentals
2. PostgreSQL setup
3. Python + PostgreSQL connection
4. CRUD operations
5. Spending analytics
6. Spending pattern detection
7. Smart / AI-style features
8. Testing and security
9. Git and GitHub

Building it this way helped me understand how different parts of a real application fit together.

## 🔮 Future Improvements

Some features I would like to work on next:

* Interactive dashboard
* Data visualization
* Budget management
* Expense forecasting
* Machine-learning based spending prediction
* LLM-powered expense assistant
* User authentication
* Multiple-user support
* REST API
* Cloud deployment

## 👨‍💻 About

Built by **Nikhil Gawade** as a practical project to strengthen skills in:

**Python • PostgreSQL • SQL • Data Analytics • Cybersecurity • Git/GitHub**.

This project is part of my journey of learning by building real projects and improving them step by step.
