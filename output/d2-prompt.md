# System Architecture Diagram Generation Prompt

You are an expert software architect tasked with creating a comprehensive system architecture diagram using D2 (diagram as code language).

## Project Overview

**Project Path**: Simple-Banking-System

## Project Structure

```
Simple-Banking-System
├── bank.py
├── client.py
└── main.py

```

## Codebase Analysis

### Files and Components

---
`bank.py`:

```py
class Bank:

    name = 'International Bank'
    clients = []

    def update_db(self, client):
        self.clients.append(client)

    def authentication(self, name, account_number):
        for i in range(len(self.clients)):
            if name in self.clients[i].account.values() and account_number in self.clients[i].account.values():
                print()
                print("Authentication successful!")
                return self.clients[i]

```

---
`client.py`:

```py
from random import randint


class Client:

    # {account_number: xxxxx, name: "xxxxxx", holdings: xxxx}
    account = {}

    def __init__(self, name, deposit):
        self.account['account_number'] = randint(10000, 99999)
        self.account['name'] = name
        self.account['holdings'] = deposit

    def withdraw(self, amount):
        if self.account['holdings'] >= amount:
            self.account['holdings'] -= amount
            print()
            print("The sum of {} has been withdrawn from your account balance.".format(amount))
            self.balance()
        else:
            print()
            print("Not enough funds!")
            self.balance()

    def deposit(self, amount):
        self.account['holdings'] += amount
        print()
        print("The sum of {} has been added to your account balance.".format(amount))
        self.balance()

    def balance(self):
        print()
        print("Your current account balance is: {} ".format(self.account['holdings']))

```

---
`main.py`:

```py
from client import Client
from bank import Bank


bank = Bank()
print()
print("Welcome to {}!".format(bank.name))
print()
running = True
while running:
    print()
    print("""Choose an option:
    
    1. Open new bank account
    2. Open existing bank account
    3. Exit
    """)

    choice = int(input("1, 2 or 3: "))

    if choice == 1:
        print()
        print("To create an account, please fill in the information below.")
        print()
        client = Client(input("Name: "), int(input("Deposit amount: ")))
        bank.update_db(client)
        print()
        print("Account created successfully! Your account number is: ", client.account['account_number'])
    elif choice == 2:
        print()
        print("To access your account, please enter your credentials below.")
        print()
        name = input("Name: ")
        account_number = int(input("Account number: "))
        current_client = bank.authentication(name, account_number)
        if current_client:
            print()
            print("Welcome {}!".format(current_client.account['name']))
            acc_open = True
            while acc_open:
                print()
                print("""Choose an option:
                
    1. Withdraw
    2. Deposit
    3. Balance
    4. Exit
                    """)
                acc_choice = int(input("1, 2, 3 or 4: "))
                if acc_choice == 1:
                    print()
                    current_client.withdraw(int(input("Withdraw amount: ")))
                elif acc_choice == 2:
                    print()
                    current_client.deposit(int(input("Deposit amount: ")))
                elif acc_choice == 3:
                    print()
                    current_client.balance()
                elif acc_choice == 4:
                    print()
                    print("Thank you for visiting!")
                    current_client = ''
                    acc_open = False
        else:
            print()
            print("Authentication failed!")
            print("Reason: account not found.")
            continue
    elif choice == 3:
        print()
        print("Goodbye!")
        running = False

```


## Your Task

Based on the codebase structure and file contents provided above, create a **system architecture diagram** using D2 syntax that illustrates:

1. **Main architectural layers** (e.g., Frontend, API, Data Layer, External Services)
2. **Key components and modules** (pages, layouts, components, utilities, APIs)
3. **Data flow** and interactions between components
4. **External dependencies** (frameworks, libraries, services)
5. **Component relationships** and hierarchy

### D2 Diagram Requirements:

- Use containers to group related components
- Show clear connections with labeled arrows indicating data flow
- Include all major directories as architectural components
- Highlight important patterns (e.g., layouts wrapping pages, API endpoints, content management)
- Use proper D2 syntax with shapes, styles, and directions
- Add a title and legend if necessary

### D2 Syntax Guidelines:

```d2
# Use this format:
component1 -> component2: relationship label
container: {
  nested_component
  nested_component2
}
```

### Focus Areas:

- **Frontend Architecture**: How pages, layouts, and components are organized
- **Content Management**: Blog posts, markdown processing, and content configuration
- **Routing**: Page structure and navigation
- **Utilities**: Helper functions and their usage across the app
- **External Integrations**: Any APIs, external services, or third-party integrations
- **Build Process**: Framework configuration and build pipeline

## Output Format

Provide:
1. A brief architectural overview (2-3 paragraphs)
2. The complete D2 diagram code
3. Key architectural decisions and patterns identified

**Generate the D2 diagram now.**