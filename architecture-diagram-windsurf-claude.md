# Simple Banking System - Architecture Diagram

## System Architecture Overview

```mermaid
graph TB
    subgraph "User Interface Layer"
        UI[Main Program<br/>main.py]
    end
    
    subgraph "Business Logic Layer"
        Bank[Bank Class<br/>bank.py]
        Client[Client Class<br/>client.py]
    end
    
    subgraph "Data Layer"
        DB[(In-Memory Database<br/>clients list)]
        Account[(Account Dictionary<br/>account_number, name, holdings)]
    end
    
    UI -->|Creates instance| Bank
    UI -->|Creates new| Client
    UI -->|Calls methods| Bank
    UI -->|Calls methods| Client
    Bank -->|Stores| DB
    Bank -->|Authenticates| Client
    Client -->|Manages| Account
    DB -->|Contains| Client
```

## Class Diagram

```mermaid
classDiagram
    class Bank {
        +String name
        +List~Client~ clients
        +update_db(client)
        +authentication(name, account_number)
    }
    
    class Client {
        +Dict account
        +__init__(name, deposit)
        +withdraw(amount)
        +deposit(amount)
        +balance()
    }
    
    class Main {
        +bank: Bank
        +running: bool
        +main_loop()
    }
    
    Main --> Bank : uses
    Main --> Client : creates
    Bank "1" --> "*" Client : manages
    Client --> Account : contains
    
    class Account {
        <<dictionary>>
        +int account_number
        +String name
        +int holdings
    }
```

## Sequence Diagram - Create Account Flow

```mermaid
sequenceDiagram
    actor User
    participant Main
    participant Bank
    participant Client
    
    User->>Main: Select "Open new account"
    Main->>User: Request name and deposit
    User->>Main: Provide name and deposit
    Main->>Client: new Client(name, deposit)
    Client->>Client: Generate account_number (10000-99999)
    Client->>Client: Initialize account dict
    Client-->>Main: Return client instance
    Main->>Bank: update_db(client)
    Bank->>Bank: Append to clients list
    Main->>User: Display account_number
```

## Sequence Diagram - Authentication & Transaction Flow

```mermaid
sequenceDiagram
    actor User
    participant Main
    participant Bank
    participant Client
    
    User->>Main: Select "Open existing account"
    Main->>User: Request credentials
    User->>Main: Provide name and account_number
    Main->>Bank: authentication(name, account_number)
    Bank->>Bank: Search in clients list
    alt Account Found
        Bank-->>Main: Return client instance
        Main->>User: Display welcome message
        User->>Main: Select operation (withdraw/deposit/balance)
        Main->>Client: Call method (withdraw/deposit/balance)
        Client->>Client: Update holdings
        Client-->>User: Display result
    else Account Not Found
        Bank-->>Main: Return None
        Main->>User: Display "Authentication failed"
    end
```

## Component Architecture

```mermaid
graph LR
    subgraph "Simple Banking System"
        A[main.py<br/>Entry Point] --> B[bank.py<br/>Bank Management]
        A --> C[client.py<br/>Account Operations]
        B -.->|stores| C
    end
    
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#ffe1f5
```

## Data Flow Diagram

```mermaid
flowchart TD
    Start([User Starts Program]) --> Menu{Main Menu}
    
    Menu -->|Option 1| Create[Create New Account]
    Menu -->|Option 2| Login[Login to Existing Account]
    Menu -->|Option 3| Exit([Exit Program])
    
    Create --> InputNew[Input: Name, Deposit]
    InputNew --> GenAccount[Generate Account Number]
    GenAccount --> StoreDB[Store in Bank Database]
    StoreDB --> ShowAccount[Display Account Number]
    ShowAccount --> Menu
    
    Login --> InputCred[Input: Name, Account Number]
    InputCred --> Auth{Authenticate}
    
    Auth -->|Success| AccMenu{Account Menu}
    Auth -->|Fail| AuthFail[Show Error]
    AuthFail --> Menu
    
    AccMenu -->|Withdraw| WithdrawOp[Withdraw Operation]
    AccMenu -->|Deposit| DepositOp[Deposit Operation]
    AccMenu -->|Balance| BalanceOp[Check Balance]
    AccMenu -->|Exit| Menu
    
    WithdrawOp --> CheckFunds{Sufficient Funds?}
    CheckFunds -->|Yes| DeductAmount[Deduct Amount]
    CheckFunds -->|No| InsufficientMsg[Show Insufficient Funds]
    DeductAmount --> ShowBalance[Show Balance]
    InsufficientMsg --> ShowBalance
    ShowBalance --> AccMenu
    
    DepositOp --> AddAmount[Add Amount]
    AddAmount --> ShowBalance
    
    BalanceOp --> ShowBalance
```

## Technology Stack

```mermaid
graph TB
    subgraph "Programming Language"
        Python[Python 3.x]
    end
    
    subgraph "Core Modules"
        Random[random.randint<br/>Account Number Generation]
    end
    
    subgraph "Design Patterns"
        OOP[Object-Oriented Programming]
        CLI[Command Line Interface]
    end
    
    Python --> OOP
    Python --> Random
    OOP --> CLI
```

## Key Features

1. **Account Management**
   - Create new bank accounts with unique 5-digit account numbers
   - Automatic account number generation (10000-99999)
   - Initial deposit requirement

2. **Authentication**
   - Name and account number based authentication
   - Secure account access

3. **Banking Operations**
   - Withdraw funds (with balance validation)
   - Deposit funds
   - Check account balance

4. **Data Storage**
   - In-memory database using Python lists
   - Account information stored in dictionaries

## Architecture Characteristics

- **Pattern**: Layered Architecture
- **Paradigm**: Object-Oriented Programming
- **Interface**: Command Line Interface (CLI)
- **Data Storage**: In-Memory (List of Dictionaries)
- **Authentication**: Simple credential matching
- **State Management**: Instance-based state in Client objects
