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
        'include_patterns': ['*.py'],
        'exclude_patterns': ['__pycache__/*', 'venv/*', '*.pyc', '*_executor.py', 'example_*.py'],
        'line_numbers': True,
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
            'include_patterns': ['*.py'],
            'exclude_patterns': ['__pycache__/*', 'venv/*', '*.pyc', '*_executor.py', 'example_*.py'],
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
        'line_numbers': True,
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
        'include_patterns': ['*.py'],
        'exclude_patterns': ['__pycache__/*', 'venv/*', '*.pyc', '*_executor.py', 'example_*.py'],
        'display_tokens': True,
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
        'include_patterns': ['*.py'],
        'exclude_patterns': ['__pycache__/*', 'venv/*', '*.pyc'],
        'line_numbers': True,
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

