# System Architecture Analysis Prompt (DSL Text Output)

Analyze the following codebase and create a structured text representation of the system architecture using a simple Domain-Specific Language (DSL) format.

## Output Format: Architecture DSL

Generate a text document using the following DSL syntax:

```
PROJECT: [project name]
TYPE: [architecture type - layered, microservices, mvc, etc.]
DESCRIPTION: [brief description]

---

LAYER: [Layer Name] (order: [number])
  
  COMPONENT: [Component Name]
    FILE: [filename or path]
    TYPE: [class, module, service, data_store, etc.]
    DESCRIPTION: [brief description]
    RESPONSIBILITIES:
      - [responsibility 1]
      - [responsibility 2]
    METHODS:
      - [method 1]
      - [method 2]
    ATTRIBUTES:
      - [attribute 1]
      - [attribute 2]

  COMPONENT: [Another Component]
    ...

LAYER: [Next Layer Name] (order: [number])
  ...

---

RELATIONSHIPS:

  [component_id] -> [component_id]
    TYPE: [relationship type]
    DESCRIPTION: [description]
    CARDINALITY: [1:1, 1:N, N:M]
    EVIDENCE: [code snippet or reference]

  [component_id] -> [component_id]
    TYPE: [relationship type]
    ...

---

DATA_FLOWS:

  FLOW: [Flow Name]
    PATH: [component1] -> [component2] -> [component3]
    DESCRIPTION: [description of data flow]

  FLOW: [Another Flow]
    ...

---

EXTERNAL_DEPENDENCIES:
  - [module/library name]: [usage description] (used by: [component_id])

---

DESIGN_PATTERNS:
  - [pattern name]
  - [pattern name]
```

## Analysis Steps:

### Step 1: Identify Components
For each file/module in the codebase:
- Assign a unique ID (lowercase, underscore-separated, e.g., `ui_main`, `bank`, `client`)
- Determine its name and role
- Identify its type (class, module, service, data_store, etc.)
- List key responsibilities (what it does)
- Note important methods/functions
- List key attributes/properties

### Step 2: Determine Architectural Layers
Group components into layers based on their role:

**Common Layers (top to bottom):**
- **Presentation/UI Layer** (order: 1): User-facing components, CLI, web interfaces
- **Business Logic Layer** (order: 2): Core domain logic, services, business rules
- **Data Layer** (order: 3): Data storage, models, repositories
- **External Services Layer** (order: 4): Third-party integrations, APIs

### Step 3: Map Relationships
For each component, identify how it interacts with others.

**Relationship Types:**
- `imports`: Module A imports module B
- `creates_instance`: A instantiates B (single instance)
- `creates_new`: A creates new instances of B (multiple)
- `calls_methods`: A invokes methods on B
- `inherits`: A extends/inherits from B
- `stores`: A persists/saves B
- `manages`: A controls lifecycle of B
- `authenticates`: A validates B
- `depends_on`: A requires B to function
- `contains`: A holds collection of B
- `uses`: Generic usage relationship
- `reads_from`: A reads data from B
- `writes_to`: A writes data to B

**Cardinality:**
- `1:1`: One-to-one relationship
- `1:N`: One-to-many relationship
- `N:M`: Many-to-many relationship

### Step 4: Trace Data Flow
Identify major data flows through the system:
- User input flows
- Data processing pipelines
- Storage operations
- External API interactions

### Step 5: Document Dependencies & Patterns
- List external libraries/modules used
- Identify design patterns employed

## Analysis Criteria:

### 1. Read Entry Points
Start with main entry files (main.py, app.py, index.js, etc.):
- What modules are imported?
- What objects are instantiated?
- What is the main execution flow?

### 2. Analyze Each Module/Class
For each file:
- What is its primary responsibility?
- What other components does it use?
- What data structures does it manage?
- What methods does it expose?

### 3. Identify Dependencies
Look for:
- Import statements
- Constructor parameters
- Method calls
- Data access patterns
- Inheritance relationships

### 4. Determine Layer Placement
Ask these questions:
- Does it handle user interaction? → UI Layer
- Does it implement business rules? → Logic Layer
- Does it manage data storage? → Data Layer
- Does it integrate external services? → External Layer

### 5. Document Relationships
For each relationship:
- Direction of dependency (who depends on whom)
- Type of relationship (creates, calls, stores, etc.)
- Cardinality (how many instances)
- Code evidence (actual code that shows the relationship)

## Example Output:

```
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
    EVIDENCE: current_client.withdraw(amount), current_client.deposit(amount)

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
    EVIDENCE: self.account['holdings'] += amount

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

  FLOW: Transaction Flow
    PATH: ui_main -> client -> account_dict
    DESCRIPTION: User initiates transaction → Client method updates account holdings → Balance displayed

---

EXTERNAL_DEPENDENCIES:
  - random.randint: Generate unique 5-digit account numbers (used by: client)

---

DESIGN_PATTERNS:
  - Object-Oriented Programming
  - Layered Architecture
  - In-Memory Repository Pattern
  - Command-Line Interface Pattern
```

## Validation Checklist:

Before finalizing the output, verify:

- [ ] All components have unique IDs
- [ ] All relationships reference valid component IDs
- [ ] Layers are ordered logically (UI → Logic → Data)
- [ ] Each component has clear, non-overlapping responsibilities
- [ ] Relationship types accurately describe interactions
- [ ] Code evidence supports each relationship claim
- [ ] Data flows are complete and logical
- [ ] No circular dependencies at layer level
- [ ] External dependencies are documented
- [ ] Design patterns are accurately identified

## Tips for Accurate Analysis:

1. **Start with imports**: They reveal dependencies immediately
2. **Follow the data**: Track how data is created, transformed, and stored
3. **Identify entry points**: Main functions, route handlers, event listeners
4. **Look for patterns**: Repeated structures often indicate architectural patterns
5. **Check instantiation**: `new`, `create`, constructors show object creation
6. **Trace method calls**: Function/method invocations show control flow
7. **Examine data structures**: Classes, structs, schemas define data layer
8. **Note external calls**: HTTP requests, database queries, file I/O

## Common Architecture Types:

- **Layered**: Organized in horizontal layers (UI, Logic, Data)
- **MVC**: Model-View-Controller separation
- **Microservices**: Independent, loosely-coupled services
- **Event-Driven**: Components communicate via events
- **Client-Server**: Frontend and backend separation
- **Monolithic**: Single unified codebase
- **Hexagonal**: Core logic with adapters for external systems
