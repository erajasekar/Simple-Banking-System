PROJECT: Simple Banking System
TYPE: layered
DESCRIPTION: Python OOP-based banking system with CLI interface for account management

---

LAYER: User Interface Layer (order: 1)
  
  COMPONENT: Main Program
    FILE: main.py
    TYPE: module
    DESCRIPTION: Entry point and CLI interface for banking operations
    RESPONSIBILITIES:
      - Display menu options to user
      - Handle user input and validation
      - Coordinate between Bank and Client classes
      - Manage application control flow
    METHODS:
      - main_loop
      - create_account_flow
      - login_flow
      - account_operations_flow
    ATTRIBUTES:
      - bank: Bank instance
      - running: boolean flag
      - current_client: Client instance or None

LAYER: Business Logic Layer (order: 2)
  
  COMPONENT: Bank Class
    FILE: bank.py
    TYPE: class
    DESCRIPTION: Manages bank operations and client database
    RESPONSIBILITIES:
      - Store client records in memory
      - Authenticate users by credentials
      - Manage client database operations
    METHODS:
      - update_db(client)
      - authentication(name, account_number)
    ATTRIBUTES:
      - name: String (bank name)
      - clients: List[Client] (client database)

  COMPONENT: Client Class
    FILE: client.py
    TYPE: class
    DESCRIPTION: Represents individual bank account with operations
    RESPONSIBILITIES:
      - Manage account data and state
      - Process withdrawal transactions
      - Process deposit transactions
      - Display account balance
      - Generate unique account numbers
    METHODS:
      - __init__(name, deposit)
      - withdraw(amount)
      - deposit(amount)
      - balance()
    ATTRIBUTES:
      - account: Dict (account information)

LAYER: Data Layer (order: 3)
  
  COMPONENT: In-Memory Database
    FILE: bank.py
    TYPE: data_store
    DESCRIPTION: List-based storage for client objects
    RESPONSIBILITIES:
      - Store client instances in memory
      - Provide access to client records
    ATTRIBUTES:
      - Structure: List[Client]
      - Persistence: in-memory (volatile)

  COMPONENT: Account Dictionary
    FILE: client.py
    TYPE: data_structure
    DESCRIPTION: Dictionary storing individual account information
    RESPONSIBILITIES:
      - Store account number, name, and balance
      - Provide account data access
    ATTRIBUTES:
      - account_number: int (5 digits, range 10000-99999)
      - name: string (account holder name)
      - holdings: int (account balance)

---

RELATIONSHIPS:

  ui_main -> bank
    TYPE: creates_instance
    DESCRIPTION: Creates single Bank instance at program startup
    CARDINALITY: 1:1
    EVIDENCE: bank = Bank()

  ui_main -> client
    TYPE: creates_new
    DESCRIPTION: Creates new Client instances for each account creation
    CARDINALITY: 1:N
    EVIDENCE: client = Client(input("Name: "), int(input("Deposit amount: ")))

  ui_main -> bank
    TYPE: calls_methods
    DESCRIPTION: Invokes bank operations for database updates and authentication
    CARDINALITY: 1:1
    EVIDENCE: bank.update_db(client), bank.authentication(name, account_number)

  ui_main -> client
    TYPE: calls_methods
    DESCRIPTION: Invokes client operations for transactions
    CARDINALITY: 1:1
    EVIDENCE: current_client.withdraw(amount), current_client.deposit(amount), current_client.balance()

  bank -> db_clients
    TYPE: stores
    DESCRIPTION: Persists client objects in list-based database
    CARDINALITY: 1:N
    EVIDENCE: self.clients.append(client)

  bank -> client
    TYPE: authenticates
    DESCRIPTION: Validates credentials and returns matching client instance
    CARDINALITY: 1:N
    EVIDENCE: return self.clients[i]

  client -> account_dict
    TYPE: manages
    DESCRIPTION: Creates and modifies account dictionary data
    CARDINALITY: 1:1
    EVIDENCE: self.account['holdings'] += amount, self.account['holdings'] -= amount

  db_clients -> client
    TYPE: contains
    DESCRIPTION: Stores multiple client instances in list
    CARDINALITY: N:1
    EVIDENCE: clients = [] (list of Client objects)

---

DATA_FLOWS:

  FLOW: Account Creation Flow
    PATH: ui_main -> client -> account_dict -> bank -> db_clients
    DESCRIPTION: User provides name and deposit → Client instance created with account dictionary → Bank stores client in database

  FLOW: Authentication Flow
    PATH: ui_main -> bank -> db_clients -> client
    DESCRIPTION: User provides credentials → Bank searches database → Matching client returned to UI

  FLOW: Transaction Flow (Withdraw/Deposit)
    PATH: ui_main -> client -> account_dict
    DESCRIPTION: User initiates transaction → Client method updates account holdings → Balance displayed

  FLOW: Balance Check Flow
    PATH: ui_main -> client -> account_dict
    DESCRIPTION: User requests balance → Client reads holdings from account dictionary → Balance displayed

---

EXTERNAL_DEPENDENCIES:
  - random.randint: Generate unique 5-digit account numbers (used by: client)

---

DESIGN_PATTERNS:
  - Object-Oriented Programming
  - Layered Architecture
  - In-Memory Repository Pattern
  - Command-Line Interface Pattern
