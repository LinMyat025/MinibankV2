#MiniBankV2

MiniBank (File-Based Banking System in Python)

A console-based mini banking application in Python that uses file handling for persistent storage, supports user registration, secure login, deposit, withdrawal, money transfer, account updates, and per-user transaction logging without using a database.

👤 Author

Developed by Lin Myat Aung
MiniBankV2 – Python File Handling Project

📌 Overview

- MiniBank is a console-based banking application written in Python.
- The project is designed for learning purposes, focusing on file handling, data structuring, and basic banking workflows without using any database.

All data is stored and managed using plain text files.

🎯 Purpose

This project was built to:
- Practice Python file handling (read, write, append, rewrite)
- Understand data flow between files and memory
- Implement basic banking logic (register, login, transfer, deposit, withdraw)
- Learn clean separation of responsibilities across modules

🔐 User Management

1. User registration with:
   - Unique account number (auto-generated)
   - Username validation
   - Strong password validation

2. Secure login using:
    - Account number
    - Username
    - Password

💰 Banking Operations

1. Deposit money
2. Withdraw money
3. Transfer money between users
    - Prevents self-transfer
    - Checks balance availability
4. Requires password confirmation

📝 Transaction Logging

Each user has a separate transaction file
Transactions include:
1. Timestamp (local time)
2. Account number
3. Transaction type
4. Amount
5. Details (TO / FROM/ +/ -)

⚙️ Account Maintenance

- Update username
- Update password
- View account information

🗂️ Project Structure

MiniBank2/
│
├── main.py                 # Entry point of the program
├── minibank2.py            # Core banking logic & menus
├── utils.py                # Utility & data processing layer
├── fileIO.py               # File handling layer
│
├── userdata.txt            # Main user data storage
├── transactions/           # Folder for per-user transaction logs
│   ├── 1000.txt
│   ├── 1001.txt
│   └── ...
│
└── README.md               # Project documentation

📄 Data Storage Design

1. userdata.txt- Stores the current snapshot of all users: account_number,username,password,balance
   Example: 1001,LinMyatAung,Linaung!@#123,45000
   This file is rewritten entirely after any data change.
2. transactions/{account_number}.txt - Stores transaction history for each user: timestamp,account_number,type,amount,details
   Example:
   2026-01-05 11:10:45,1001,TRANSFER,300,TO:1002

▶️ How to Run the Program
Requirements:
- Python 3.8+ recommended
- No external libraries required
- Run python main.py

🔒 Password Rules

A password is considered strong if:
- Minimum 8 characters
- At least 2 numbers
- At least 2 special characters

🧠 Design Principles Used
- Separation of concerns
- main.py → entry point
- minibank2.py → business logic
- utils.py → data transformation & validation
- fileIO.py → file system operations
- Snapshot storage model
- In-memory processing + file rewrite
- Readable & maintainable logic over premature optimization

⚠️ Limitations

! No database (text-file based only)
! No encryption (passwords stored as plain text)
! Single-user CLI (no concurrency handling)
These limitations are intentional for learning purposes.

📚 Learning Outcome

This project demonstrates:
- Realistic file-based data management
- Error handling and input validation
- Practical Python programming patterns
- Foundation for upgrading to databases later
