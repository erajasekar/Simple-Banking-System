PROJECT: Simple Banking System
TYPE: layered

---

LAYERS:

User Interface Layer:
  - Main Program (main.py)

Business Logic Layer:
  - Bank Class (bank.py)
  - Client Class (client.py)

Data Layer:
  - In-Memory Database (bank.py)
  - Account Dictionary (client.py)

---

RELATIONSHIPS:

Main Program -> Bank Class: creates
Main Program -> Client Class: creates
Main Program -> Bank Class: calls
Main Program -> Client Class: calls
Bank Class -> In-Memory Database: stores
Bank Class -> Client Class: authenticates
Client Class -> Account Dictionary: manages
In-Memory Database -> Client Class: contains

---

SUMMARY:
A 3-layer Python banking system with CLI interface (main.py) that coordinates Bank and Client classes for account management. Bank class manages client database and authentication, while Client class handles individual account operations. Data is stored in-memory using lists and dictionaries.
