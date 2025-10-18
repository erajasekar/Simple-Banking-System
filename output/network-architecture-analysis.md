# System Architecture Analysis for Diagram Generation

## Project Information
- **Project Path**: Simple-Banking-System
- **Analysis Date**: Generated using code2prompt

## Project Structure Overview

```
Simple-Banking-System
├── bank.py
├── client.py
└── main.py

```

## Detailed Codebase Analysis

### Files and Components

---

#### File: `bank.py`


##### Content:

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

#### File: `client.py`


##### Content:

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

#### File: `main.py`


##### Content:

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


---

## Instructions for LLM: Extract Key Information and Generate Concise Diagram Prompt

**IMPORTANT**: Your task is NOT to create a diagram directly. Instead:

1. **Analyze the source code above** and extract ONLY the essential information for a simple network architecture diagram
2. **Generate concise, token-optimized instructions** for another LLM to create the diagram WITHOUT the source code
3. **Focus on clarity over completeness** - include only what's necessary for a clear, simple diagram
4. **Minimize token count** - use bullet points, abbreviations, and efficient formatting

**CRITICAL RULE**: 
- **DO NOT make up, infer, or assume anything**
- **ONLY include information that explicitly exists in the source code**
- If something is not present in the code, DO NOT include it in your output
- Extract facts directly from the code - no interpretation or assumptions


### For Network Architecture Diagram - Extract Essentials:

**Extract:**
- Network components (servers, clients, load balancers, proxies, firewalls, routers)
- Network topology and zones (DMZ, internal, external)
- Connection protocols (HTTP, HTTPS, TCP, UDP, WebSocket, gRPC)
- IP addresses, ports, and endpoints if explicitly defined
- Security boundaries and authentication points
- Network flows and communication paths

**Output:**
Concise prompt with: network nodes, connections with protocols/ports, security zones. Format as "Node A --[protocol:port]--> Node B".
---

## Summary

**Your Task:** Extract ONLY essential network architecture information that actually exists in the source code above. Generate a simple, token-efficient prompt for another LLM to create a basic network architecture diagram. 

**Remember:**
- Extract only what's explicitly in the code - no assumptions or inferences
- Prioritize brevity and clarity - use abbreviations, bullet points, minimal formatting
- Keep output as short as possible while maintaining accuracy
- If in doubt, exclude rather than make assumptions