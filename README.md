MiniBank (File-Based Banking System in Python)
==============================================

A console-based mini banking application in Python that uses file handling for
persistent storage. It supports user registration, secure login, deposit,
withdrawal, money transfer, account updates, and per-user transaction logging
without using a database.

Author
------

Developed by Lin Myat Aung

MiniBankV2 - Python File Handling Project

Overview
--------

- MiniBank is a console-based banking application written in Python.
- The project is designed for learning purposes, focusing on file handling,
  data structuring, and basic banking workflows without using any database.
- All data is stored and managed using plain text files.
- The file handling layer automatically creates the required storage files and
  folders when the program starts.

Purpose
-------

This project was built to:

- Practice Python file handling: read, write, append, and rewrite.
- Understand data flow between files and memory.
- Implement basic banking logic: register, login, transfer, deposit, and
  withdraw.
- Learn clean separation of responsibilities across modules.

User Management
---------------

1. User registration with:
   - Unique account number, auto-generated.
   - Username validation.
   - Strong password validation.

2. Secure login using:
   - Account number.
   - Username.
   - Password.

Banking Operations
------------------

1. Deposit money.
2. Withdraw money.
3. Transfer money between users.
   - Prevents self-transfer.
   - Checks balance availability.
4. Requires password confirmation for banking actions.

Transaction Logging
-------------------

Each user has a separate transaction file. Transactions include:

1. Timestamp, using local time.
2. Account number.
3. Transaction type.
4. Amount.
5. Details: TO, FROM, +, or -.

Account Maintenance
-------------------

- Update username.
- Update password.
- View account information.

Project Structure
-----------------

```text
MiniBank2/
|-- main.py                 # Entry point of the program
|-- minibank2.py            # Core banking logic and menus
|-- utils.py                # Utility and data processing layer
|-- fileIO.py               # File handling layer
|-- userdata.txt            # Main user data storage, auto-created if missing
|-- transactions/           # Transaction logs folder, auto-created if missing
|   |-- 1000.txt
|   |-- 1001.txt
|   `-- ...
`-- README.md               # Project documentation
```

Data Storage Design
-------------------

1. `userdata.txt`

   Stores the current snapshot of all users:

   ```text
   account_number,username,password,balance
   ```

   Example:

   ```text
   1001,LinMyatAung,Linaung!@#123,45000
   ```

   This file is rewritten entirely after any account data change. If the file is
   missing, `fileIO.py` creates it automatically.

2. `transactions/{account_number}.txt`

   Stores transaction history for each user:

   ```text
   timestamp,account_number,type,amount,details
   ```

   Example:

   ```text
   2026-01-05 11:10:45,1001,TRANSFER,300,TO:1002
   ```

   The `transactions/` folder is created automatically if it is missing. A new
   user transaction file is created during registration.

How to Run the Program
----------------------

Requirements:

- Python 3.8+ recommended.
- No external libraries required.

Run:

```bash
python main.py
```

Storage setup is automatic. You do not need to manually create `userdata.txt` or
the `transactions/` folder before running the program.

Password Rules
--------------

A password is considered strong if it has:

- Minimum 8 characters.
- At least 2 numbers.
- At least 2 special characters.

Design Principles Used
----------------------

- Separation of concerns.
- `main.py` -> entry point.
- `minibank2.py` -> business logic.
- `utils.py` -> data transformation and validation.
- `fileIO.py` -> file system operations.
- Snapshot storage model.
- In-memory processing plus file rewrite.
- Readable and maintainable logic over premature optimization.

Limitations
-----------

- No database, text-file based only.
- No encryption, passwords are stored as plain text.
- Single-user CLI, no concurrency handling.

These limitations are intentional for learning purposes.

Learning Outcome
----------------

This project demonstrates:

- Realistic file-based data management.
- Error handling and input validation.
- Practical Python programming patterns.
- Foundation for upgrading to databases later.
