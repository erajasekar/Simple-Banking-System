# System Architecture Analysis for Diagram Generation

## Project Information
- **Project Path**: Simple-Banking-System
- **Analysis Date**: Generated using code2prompt

## Project Structure Overview

```
Simple-Banking-System
├── client.py
├── code2prompt_executor.py
├── bank.py
├── example_usage.py
├── main.py
└── test_sdk_integration.py

```

## Detailed Codebase Analysis

### Files and Components

---

#### File: `Simple-Banking-System/client.py`


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

#### File: `Simple-Banking-System/code2prompt_executor.py`


##### Content:

```py
"""
Code2Prompt Programmatic Executor
This script executes code2prompt programmatically using the CLI tool.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
from typing import Optional, List, Dict, Any
import json
from code2prompt_rs import Code2Prompt


class Code2PromptExecutor:
    """Execute code2prompt programmatically with custom configuration using the Python SDK."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the Code2Prompt executor.
        
        Args:
            config: Configuration dictionary with options like:
                - path: Path to analyze (required)
                - template: Path to Handlebars/Jinja2 template file
                - output: Output file path
                - filter: File patterns to include (e.g., "*.py,*.js")
                - exclude: Patterns to exclude
                - line_number: Add line numbers (bool)
                - suppress_comments: Strip comments (bool)
                - encoding: File encoding (default: utf-8)
                - tokens: Display token count (bool)
        """
        self.config = config or {}
        self.validate_config()
    
    def validate_config(self):
        """Validate the configuration."""
        if not self.config.get('path'):
            raise ValueError("Configuration must include 'path' parameter")
        
        path = Path(self.config['path'])
        if not path.exists():
            raise FileNotFoundError(f"Path does not exist: {path}")
        
        # Validate template if provided
        if self.config.get('template'):
            template = Path(self.config['template'])
            if not template.exists():
                raise FileNotFoundError(f"Template file does not exist: {template}")
    
    def _convert_config_to_sdk_params(self) -> Dict[str, Any]:
        """
        Convert our config format to the SDK's expected parameters.
        
        Returns:
            Dictionary with SDK-compatible parameters
        """
        sdk_config = {}
        
        # Required: path
        sdk_config['path'] = str(self.config['path'])
        
        # Include patterns (convert from 'filter' to 'include_patterns')
        if self.config.get('filter'):
            # Split comma-separated patterns
            patterns = [p.strip() for p in self.config['filter'].split(',')]
            sdk_config['include_patterns'] = patterns
        
        # Exclude patterns
        if self.config.get('exclude'):
            # Split comma-separated patterns
            patterns = [p.strip() for p in self.config['exclude'].split(',')]
            sdk_config['exclude_patterns'] = patterns
        
        # Line numbers
        if self.config.get('line_number'):
            sdk_config['line_numbers'] = True
        
        # Suppress comments
        if self.config.get('suppress_comments'):
            sdk_config['suppress_comments'] = True
        
        # Encoding
        if self.config.get('encoding'):
            sdk_config['encoding'] = self.config['encoding']
        
        # Token display
        if self.config.get('tokens'):
            sdk_config['display_tokens'] = True
        
        return sdk_config
    
    def execute(self) -> str:
        """
        Execute code2prompt using the Python SDK and return the output.
        
        Returns:
            The generated prompt as a string
        
        Raises:
            Exception: If code2prompt execution fails
        """
        try:
            # Convert config to SDK parameters
            sdk_params = self._convert_config_to_sdk_params()
            
            print(f"RAJA DEBUG: Starting execute() method")
            print(f"RAJA DEBUG: Config = {self.config}")
            print(f"RAJA DEBUG: SDK params = {sdk_params}")
            
            print(f"Executing Code2Prompt SDK with path: {sdk_params.get('path')}")
            if sdk_params.get('include_patterns'):
                print(f"  Include patterns: {sdk_params.get('include_patterns')}")
            if sdk_params.get('exclude_patterns'):
                print(f"  Exclude patterns: {sdk_params.get('exclude_patterns')}")
            if self.config.get('template'):
                print(f"  Template: {self.config.get('template')}")
                print(f"RAJA DEBUG: Template path exists: {Path(self.config['template']).exists()}")
                print(f"RAJA DEBUG: Template absolute path: {Path(self.config['template']).absolute()}")
            
            # Create Code2Prompt instance with SDK parameters
            print(f"RAJA DEBUG: Creating Code2Prompt instance")
            c2p = Code2Prompt(**sdk_params)
            print(f"RAJA DEBUG: Code2Prompt instance created successfully")
            
            # Generate the prompt using the SDK
            # The generate() method returns a RenderedPrompt object with .prompt attribute
            print(f"RAJA DEBUG: Calling generate() method")
            if self.config.get('template'):
                template_path = Path(self.config['template'])
                print(f"RAJA DEBUG: Generating with template: {template_path}")
                
                # Read the template content as a string (SDK expects template content, not path)
                template_content = template_path.read_text(encoding='utf-8')
                print(f"RAJA DEBUG: Template loaded, length: {len(template_content)} chars")
                
                # Check if it's a Jinja2 template and suggest using Handlebars
                if template_path.suffix == '.j2':
                    print(f"RAJA DEBUG: Warning - .j2 template detected. SDK uses Handlebars by default.")
                    print(f"RAJA DEBUG: Consider using .hbs version if available: {template_path.with_suffix('.hbs')}")
                    
                    # Check if .hbs version exists
                    hbs_template = template_path.with_suffix('.hbs')
                    if hbs_template.exists():
                        print(f"RAJA DEBUG: Found .hbs version, using that instead")
                        template_content = hbs_template.read_text(encoding='utf-8')
                        template_path = hbs_template
                
                # Generate with template content
                rendered = c2p.generate(template=template_content)
                print(f"RAJA DEBUG: Generate completed with template")
                prompt_text = rendered.prompt
            else:
                print(f"RAJA DEBUG: Generating without template")
                rendered = c2p.generate()
                print(f"RAJA DEBUG: Generate completed without template")
                prompt_text = rendered.prompt
            
            print(f"RAJA DEBUG: Prompt text type: {type(prompt_text)}")
            print(f"RAJA DEBUG: Prompt text is string: {isinstance(prompt_text, str)}")
            print(f"RAJA DEBUG: Prompt text length: {len(prompt_text)}")
            print(f"RAJA DEBUG: First 200 chars of prompt: {prompt_text[:200]}")
            print(f"RAJA DEBUG: Last 200 chars of prompt: {prompt_text[-200:]}")
            
            # If output file is specified, write to file
            if self.config.get('output'):
                output_file = Path(self.config['output'])
                output_file.parent.mkdir(parents=True, exist_ok=True)
                
                print(f"RAJA DEBUG: Writing to output file: {output_file}")
                print(f"RAJA DEBUG: About to write {len(prompt_text)} characters")
                
                output_file.write_text(prompt_text, encoding='utf-8')
                
                print(f"RAJA DEBUG: File written successfully")
                print(f"RAJA DEBUG: Verifying file contents...")
                verification = output_file.read_text(encoding='utf-8')
                print(f"RAJA DEBUG: File contains {len(verification)} characters")
                print(f"RAJA DEBUG: File first 200 chars: {verification[:200]}")
                
                print(f"  Output written to: {output_file}")
            
            return prompt_text
                
        except Exception as e:
            print(f"RAJA DEBUG: Exception caught: {type(e).__name__}")
            print(f"RAJA DEBUG: Exception message: {str(e)}")
            import traceback
            print(f"RAJA DEBUG: Traceback:\n{traceback.format_exc()}")
            print(f"Error executing code2prompt SDK: {e}")
            raise
    
    def execute_with_template(self, template: str, output_path: Optional[str] = None) -> str:
        """
        Execute code2prompt with a specific template.
        
        Args:
            template: Path to the Handlebars/Jinja2 template file
            output_path: Optional output file path
        
        Returns:
            The generated prompt as a string
        """
        self.config['template'] = template
        
        if output_path:
            self.config['output'] = output_path
        
        return self.execute()


def main():
    """Example usage of Code2PromptExecutor."""
    
   
    # Example 2: Different diagram types
    print("=" * 80)
    print("Example 2: Generate flowchart description")
    print("=" * 80)
    
    config2 = {
        'path': '.',
        'template': 'generate-diagram-description-flowchart.j2',
        'output': 'output/flowchart-analysis.md',
        'filter': '*.py'
    }
    
    try:
        executor2 = Code2PromptExecutor(config2)
        result2 = executor2.execute()
        print(f"\n✓ Successfully generated flowchart prompt: {result2}")
        print(f"  Output saved to: {config2['output']}")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return 1
    
    print()
    print("=" * 80)
    print("All examples completed successfully!")
    print("=" * 80)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())


```

---

#### File: `Simple-Banking-System/bank.py`


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

#### File: `Simple-Banking-System/example_usage.py`


##### Content:

```py
#!/usr/bin/env python3
"""
Quick example demonstrating code2prompt usage with the Banking System project.
"""

from code2prompt_executor import Code2PromptExecutor
from pathlib import Path
import json


def example_1_single_diagram_type():
    """Generate a UML class diagram prompt for the banking system."""
    print("\n" + "="*80)
    print("Example 1: Generate UML Class Diagram Prompt")
    print("="*80 + "\n")
    
    config = {
        'path': '.',
        'template': 'generate-diagram-description.j2',
        'output': 'output/banking-uml-prompt.md',
        'filter': '*.py',
        'exclude': '__pycache__/*,venv/*,*.pyc,*_executor.py,example_*.py',
        'line_number': True,
        'variables': {
            'diagramType': 'uml'
        }
    }
    
    executor = Code2PromptExecutor(config)
    result = executor.execute()
    
    print(f"✓ Generated UML diagram prompt")
    print(f"  Output: {config['output']}")
    print(f"  Size: {len(result):,} characters\n")


def example_2_all_diagram_types():
    """Generate prompts for all diagram types."""
    print("\n" + "="*80)
    print("Example 2: Generate All Diagram Types")
    print("="*80 + "\n")
    
    diagram_types = {
        'uml': 'UML Class Diagram',
        'flowchart': 'Flowchart',
        'sequence': 'Sequence Diagram',
        'erd': 'Entity Relationship Diagram'
    }
    
    for diagram_type, description in diagram_types.items():
        config = {
            'path': '.',
            'template': 'generate-diagram-description.j2',
            'output': f'output/{diagram_type}-prompt.md',
            'filter': '*.py',
            'exclude': '__pycache__/*,venv/*,*.pyc,*_executor.py,example_*.py',
            'variables': {
                'diagramType': diagram_type
            }
        }
        
        executor = Code2PromptExecutor(config)
        result = executor.execute()
        
        print(f"✓ {description:30} → output/{diagram_type}-prompt.md")
    
    print()


def example_3_specific_files():
    """Generate prompt for specific files only."""
    print("\n" + "="*80)
    print("Example 3: Analyze Specific Files (Core Banking System)")
    print("="*80 + "\n")
    
    # Only analyze the core banking system files
    config = {
        'path': ['bank.py', 'client.py', 'main.py'],
        'template': 'generate-diagram-description.j2',
        'output': 'output/core-banking-uml.md',
        'line_number': True,
        'variables': {
            'diagramType': 'uml'
        }
    }
    
    executor = Code2PromptExecutor(config)
    result = executor.execute()
    
    print(f"✓ Generated UML prompt for core banking files")
    print(f"  Files analyzed: bank.py, client.py, main.py")
    print(f"  Output: {config['output']}")
    print(f"  Size: {len(result):,} characters\n")


def example_4_with_token_counting():
    """Generate prompt with token counting."""
    print("\n" + "="*80)
    print("Example 4: Generate with Token Counting")
    print("="*80 + "\n")
    
    config = {
        'path': '.',
        'template': 'generate-diagram-description.j2',
        'output': 'output/sequence-with-tokens.md',
        'filter': '*.py',
        'exclude': '__pycache__/*,venv/*,*.pyc,*_executor.py,example_*.py',
        'tokens': True,
        'encoding': 'cl100k_base',  # GPT-4 encoding
        'variables': {
            'diagramType': 'sequence'
        }
    }
    
    executor = Code2PromptExecutor(config)
    result = executor.execute()
    
    print(f"✓ Generated sequence diagram prompt with token counting")
    print(f"  Output: {config['output']}")
    print(f"  Encoding: {config['encoding']}")
    print(f"  Check the output for token count information\n")


def example_5_load_from_json_config():
    """Load configuration from JSON file."""
    print("\n" + "="*80)
    print("Example 5: Load Configuration from JSON File")
    print("="*80 + "\n")
    
    # Create a sample config file
    sample_config = {
        'path': '.',
        'template': 'generate-diagram-description.j2',
        'output': 'output/flowchart-from-config.md',
        'filter': '*.py',
        'exclude': '__pycache__/*,venv/*,*.pyc',
        'line_number': True,
        'suppress_comments': False,
        'variables': {
            'diagramType': 'flowchart'
        }
    }
    
    config_file = 'config.json'
    with open(config_file, 'w') as f:
        json.dump(sample_config, f, indent=2)
    
    print(f"Created configuration file: {config_file}")
    
    # Load and use the config
    with open(config_file, 'r') as f:
        loaded_config = json.load(f)
    
    executor = Code2PromptExecutor(loaded_config)
    result = executor.execute()
    
    print(f"✓ Generated flowchart prompt from JSON config")
    print(f"  Config file: {config_file}")
    print(f"  Output: {loaded_config['output']}\n")


def main():
    """Run all examples."""
    print("\n" + "="*80)
    print("CODE2PROMPT EXECUTOR - EXAMPLES")
    print("="*80)
    
    # Ensure output directory exists
    Path('output').mkdir(exist_ok=True)
    
    try:
        # Run examples
        example_1_single_diagram_type()
        example_2_all_diagram_types()
        example_3_specific_files()
        example_4_with_token_counting()
        example_5_load_from_json_config()
        
        print("="*80)
        print("✓ All examples completed successfully!")
        print("="*80)
        print("\nGenerated files in output/ directory:")
        print("  - banking-uml-prompt.md")
        print("  - uml-prompt.md")
        print("  - flowchart-prompt.md")
        print("  - sequence-prompt.md")
        print("  - erd-prompt.md")
        print("  - core-banking-uml.md")
        print("  - sequence-with-tokens.md")
        print("  - flowchart-from-config.md")
        print("\nConfiguration file created:")
        print("  - config.json")
        print()
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())


```

---

#### File: `Simple-Banking-System/main.py`


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

#### File: `Simple-Banking-System/test_sdk_integration.py`


##### Content:

```py
#!/usr/bin/env python3
"""
Test script to verify the SDK integration.
This demonstrates that the refactored code works with the native Python SDK.
"""

from code2prompt_executor import Code2PromptExecutor
from pathlib import Path


def test_basic_usage():
    """Test basic SDK usage."""
    print("=" * 80)
    print("Test 1: Basic SDK Usage")
    print("=" * 80)
    
    config = {
        'path': '.',
        'filter': '*.py',
        'exclude': '__pycache__/*,*.pyc,test_*.py',
        'line_number': True,
    }
    
    try:
        executor = Code2PromptExecutor(config)
        result = executor.execute()
        
        print(f"\n✓ Successfully generated prompt using SDK")
        print(f"  Length: {len(result)} characters")
        print(f"  First 200 chars: {result[:200]}...")
        return True
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False


def test_with_template():
    """Test SDK with template."""
    print("\n" + "=" * 80)
    print("Test 2: SDK with Template")
    print("=" * 80)
    
    # Check if template exists
    template = Path('generate-diagram-description.j2')
    if not template.exists():
        print(f"⚠ Template not found: {template}")
        print("  Skipping template test")
        return True
    
    config = {
        'path': '.',
        'template': 'generate-diagram-description.j2',
        'output': 'output/sdk-test-output.md',
        'filter': '*.py',
        'exclude': '__pycache__/*,*.pyc',
        'variables': {
            'diagramType': 'uml'
        }
    }
    
    try:
        executor = Code2PromptExecutor(config)
        result = executor.execute()
        
        output_file = Path(config['output'])
        if output_file.exists():
            print(f"\n✓ Successfully generated prompt with template")
            print(f"  Output saved to: {output_file}")
            print(f"  File size: {output_file.stat().st_size} bytes")
            return True
        else:
            print(f"\n✗ Output file not created: {output_file}")
            return False
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False


def test_convenience_method():
    """Test the convenience method."""
    print("\n" + "=" * 80)
    print("Test 3: Convenience Method")
    print("=" * 80)
    
    template = Path('generate-diagram-description.j2')
    if not template.exists():
        print(f"⚠ Template not found: {template}")
        print("  Skipping convenience method test")
        return True
    
    config = {
        'path': '.',
        'filter': '*.py',
        'exclude': '__pycache__/*,*.pyc',
    }
    
    try:
        executor = Code2PromptExecutor(config)
        result = executor.execute_with_template_vars(
            template='generate-diagram-description.j2',
            variables={'diagramType': 'flowchart'},
            output_path='output/sdk-convenience-test.md'
        )
        
        print(f"\n✓ Successfully used convenience method")
        print(f"  Generated {len(result)} characters")
        return True
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False


def main():
    """Run all tests."""
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "Code2Prompt SDK Integration Tests" + " " * 24 + "║")
    print("╚" + "=" * 78 + "╝")
    print()
    
    results = []
    
    # Run tests
    results.append(("Basic Usage", test_basic_usage()))
    results.append(("With Template", test_with_template()))
    results.append(("Convenience Method", test_convenience_method()))
    
    # Summary
    print("\n" + "=" * 80)
    print("Test Summary")
    print("=" * 80)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {status}: {test_name}")
    
    print()
    print(f"Results: {passed}/{total} tests passed")
    print("=" * 80)
    
    return 0 if passed == total else 1


if __name__ == '__main__':
    import sys
    sys.exit(main())


```


---

## Instructions for LLM: Extract Key Information and Generate Concise Diagram Prompt

**IMPORTANT**: Your task is NOT to create a diagram directly. Instead:

1. **Analyze the source code above** and extract ONLY the essential information for a simple flowchart diagram
2. **Generate concise, token-optimized instructions** for another LLM to create the diagram WITHOUT the source code
3. **Focus on clarity over completeness** - include only what's necessary for a clear, simple diagram
4. **Minimize token count** - use bullet points, abbreviations, and efficient formatting

**CRITICAL RULE**: 
- **DO NOT make up, infer, or assume anything**
- **ONLY include information that explicitly exists in the source code**
- If something is not present in the code, DO NOT include it in your output
- Extract facts directly from the code - no interpretation or assumptions


### For Flowchart Diagram - Extract Essentials:

**Extract:**
- Main entry point and key processes (in order)
- Important decision points (conditions)
- Critical loops and I/O operations

**Output:**
Concise prompt with: start → main steps → decisions → end. List only key flow, omit minor details.
---

## Summary

**Your Task:** Extract ONLY essential flowchart-specific information that actually exists in the source code above. Generate a simple, token-efficient prompt for another LLM to create a basic flowchart diagram. 

**Remember:**
- Extract only what's explicitly in the code - no assumptions or inferences
- Prioritize brevity and clarity - use abbreviations, bullet points, minimal formatting
- Keep output as short as possible while maintaining accuracy
- If in doubt, exclude rather than make assumptions