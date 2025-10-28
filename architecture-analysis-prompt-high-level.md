# High-Level System Architecture Analysis Prompt (Simple DSL)

Analyze the following codebase and create a **high-level** architecture overview using a simple DSL format. Focus on major components and their relationships, not implementation details.

## Output Format: Simple Architecture DSL

Generate a concise text document using this DSL syntax:

```
PROJECT: [project name]
TYPE: [architecture type]

---

LAYERS:

[Layer Name]:
  - [Component Name] ([filename])
  - [Component Name] ([filename])

[Layer Name]:
  - [Component Name] ([filename])

---

RELATIONSHIPS:

[component] -> [component]: [relationship type]
[component] -> [component]: [relationship type]

---

SUMMARY:
[Brief 2-3 sentence architecture summary]
```

## Analysis Guidelines:

### 1. Identify Major Components Only
- Focus on **main files/classes** that represent distinct responsibilities
- Ignore utility functions, helpers, and implementation details
- Group related functionality into single components
- Typical components: UI/CLI, Controllers, Services, Models, Data Stores

### 2. Determine Architectural Layers
Organize components into 3-4 high-level layers:

**Common Layers:**
- **User Interface / Presentation**: Entry points, CLI, web UI, API endpoints
- **Business Logic / Application**: Core domain logic, services, controllers
- **Data / Persistence**: Data storage, models, repositories
- **External Services** (if applicable): Third-party APIs, external systems

### 3. Map Key Relationships
Focus on **primary interactions** only:

**Relationship Types (simplified):**
- `creates`: A instantiates B
- `calls`: A invokes methods on B
- `stores`: A persists B
- `manages`: A controls B
- `uses`: Generic usage (when specific type unclear)
- `contains`: A holds collection of B

**Rules:**
- Only document direct, important relationships
- Skip transitive relationships (if A→B and B→C, don't show A→C)
- Combine similar relationships (e.g., "calls methods" instead of listing each method)

## Analysis Steps:

### Step 1: Identify Entry Point
- Find main file (main.py, app.py, index.js, server.js, etc.)
- This is typically in the UI/Presentation layer

### Step 2: Find Core Business Logic
- Look for classes/modules that implement domain logic
- These handle business rules, validations, operations
- Usually in Business Logic layer

### Step 3: Locate Data Components
- Find where data is stored (databases, files, in-memory structures)
- Identify data models/schemas
- These belong in Data layer

### Step 4: Map Direct Relationships
- What does the entry point create/use?
- What does business logic interact with?
- Where is data stored and accessed?

### Step 5: Write Concise Summary
- What type of architecture is this?
- What are the main components?
- How do they interact?

## Example Output:

```
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
```

## Validation Checklist:

- [ ] Maximum 3-5 components per layer
- [ ] Maximum 3-4 layers total
- [ ] Only direct relationships shown (no transitive)
- [ ] No implementation details (methods, attributes, etc.)
- [ ] Clear, simple relationship types
- [ ] Concise summary (2-3 sentences)

## What to EXCLUDE:

- ❌ Method names and signatures
- ❌ Attribute/property details
- ❌ Code snippets or evidence
- ❌ Detailed responsibilities lists
- ❌ Data flow descriptions
- ❌ External dependencies (unless major)
- ❌ Design patterns (unless critical to understanding)
- ❌ Helper/utility functions
- ❌ Configuration files
- ❌ Test files

## What to INCLUDE:

- ✅ Main entry point(s)
- ✅ Core business logic classes/modules
- ✅ Primary data storage mechanisms
- ✅ Major external services (if any)
- ✅ Direct component interactions
- ✅ Layer organization

## Tips for High-Level Analysis:

1. **Think in terms of "boxes and arrows"** - what are the major boxes and how do they connect?
2. **Ask "What does this do?"** not "How does this work?"
3. **Combine similar components** - if you have 5 service classes, group them as "Services"
4. **Focus on architecture, not implementation** - ignore the details
5. **Keep it simple** - if you can't explain it in one sentence, it's too detailed

## Common Architecture Types:

- **layered**: Horizontal layers (UI → Logic → Data)
- **mvc**: Model-View-Controller
- **client-server**: Frontend and backend
- **microservices**: Independent services
- **monolithic**: Single unified application
- **event-driven**: Event-based communication

## Example for Different Project Types:

### Web Application:
```
LAYERS:
Frontend Layer:
  - React App (src/App.js)
  
Backend Layer:
  - Express Server (server.js)
  - API Routes (routes/)
  
Data Layer:
  - MongoDB Database
```

### Microservices:
```
LAYERS:
API Gateway Layer:
  - API Gateway (gateway/)
  
Services Layer:
  - User Service (user-service/)
  - Order Service (order-service/)
  - Payment Service (payment-service/)
  
Data Layer:
  - User Database
  - Order Database
```

### CLI Tool:
```
LAYERS:
Interface Layer:
  - CLI Handler (cli.py)
  
Logic Layer:
  - Command Processor (processor.py)
  
Data Layer:
  - Config File (config.json)
```
