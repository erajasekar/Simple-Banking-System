#!/usr/bin/env python3
"""
Code2Prompt Programmatic Executor
This script executes code2prompt programmatically using the Python SDK.
"""

import os
import subprocess
import sys
from pathlib import Path
from typing import Optional, List, Dict, Any
import json


class Code2PromptExecutor:
    """Execute code2prompt programmatically with custom configuration."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the Code2Prompt executor.
        
        Args:
            config: Configuration dictionary with options like:
                - path: Path to analyze (required)
                - template: Path to Jinja2 template file
                - output: Output file path
                - filter: File patterns to include (e.g., "*.py,*.js")
                - exclude: Patterns to exclude
                - line_number: Add line numbers (bool)
                - suppress_comments: Strip comments (bool)
                - variables: Dict of template variables
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
            template_path = Path(self.config['template'])
            if not template_path.exists():
                raise FileNotFoundError(f"Template file does not exist: {template_path}")
    
    def build_command(self) -> List[str]:
        """Build the code2prompt command from configuration."""
        cmd = ['code2prompt']
        
        # Required: path
        path = self.config['path']
        if isinstance(path, list):
            for p in path:
                cmd.extend(['--path', str(p)])
        else:
            cmd.extend(['--path', str(path)])
        
        # Optional: template
        if self.config.get('template'):
            cmd.extend(['--template', str(self.config['template'])])
        
        # Optional: output
        if self.config.get('output'):
            cmd.extend(['--output', str(self.config['output'])])
        
        # Optional: filter
        if self.config.get('filter'):
            cmd.extend(['--filter', self.config['filter']])
        
        # Optional: exclude
        if self.config.get('exclude'):
            cmd.extend(['--exclude', self.config['exclude']])
        
        # Optional: line numbers
        if self.config.get('line_number'):
            cmd.append('--line-number')
        
        # Optional: suppress comments
        if self.config.get('suppress_comments'):
            cmd.append('--suppress-comments')
        
        # Optional: encoding
        if self.config.get('encoding'):
            cmd.extend(['--encoding', self.config['encoding']])
        
        # Optional: tokens (display token count)
        if self.config.get('tokens'):
            cmd.append('--tokens')
        
        # Optional: template variables
        if self.config.get('variables'):
            for key, value in self.config['variables'].items():
                cmd.extend(['--variable', f'{key}={value}'])
        
        return cmd
    
    def execute(self) -> str:
        """
        Execute code2prompt and return the output.
        
        Returns:
            The generated prompt as a string
        
        Raises:
            subprocess.CalledProcessError: If code2prompt execution fails
        """
        cmd = self.build_command()
        
        print(f"Executing: {' '.join(cmd)}")
        
        try:
            # If output file is specified, code2prompt will write to file
            # Otherwise, capture stdout
            if self.config.get('output'):
                result = subprocess.run(
                    cmd,
                    check=True,
                    capture_output=True,
                    text=True
                )
                output_file = Path(self.config['output'])
                if output_file.exists():
                    return output_file.read_text()
                else:
                    return result.stdout
            else:
                result = subprocess.run(
                    cmd,
                    check=True,
                    capture_output=True,
                    text=True
                )
                return result.stdout
                
        except subprocess.CalledProcessError as e:
            print(f"Error executing code2prompt: {e}")
            print(f"stderr: {e.stderr}")
            raise
    
    def execute_with_template_vars(self, template_path: str, variables: Dict[str, str], output_path: Optional[str] = None) -> str:
        """
        Execute code2prompt with a specific template and variables.
        
        Args:
            template_path: Path to the Jinja2 template file
            variables: Dictionary of template variables
            output_path: Optional output file path
        
        Returns:
            The generated prompt
        """
        self.config['template'] = template_path
        self.config['variables'] = variables
        
        if output_path:
            self.config['output'] = output_path
        
        return self.execute()


def main():
    """Example usage of Code2PromptExecutor."""
    
    # Example 1: Basic usage with template
    print("=" * 80)
    print("Example 1: Generate diagram description with custom template")
    print("=" * 80)
    
    config = {
        'path': '.',  # Current directory
        'template': 'generate-diagram-description.j2',
        'output': 'output/diagram-analysis.md',
        'filter': '*.py',  # Only Python files
        'exclude': '__pycache__/*,*.pyc',
        'line_number': True,
        'variables': {
            'diagramType': 'uml'  # Can be: uml, flowchart, sequence, erd
        }
    }
    
    try:
        executor = Code2PromptExecutor(config)
        result = executor.execute()
        print(f"\n✓ Successfully generated prompt")
        print(f"  Output saved to: {config['output']}")
        print(f"  Length: {len(result)} characters")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return 1
    
    print()
    
    # Example 2: Different diagram types
    print("=" * 80)
    print("Example 2: Generate flowchart description")
    print("=" * 80)
    
    config2 = {
        'path': '.',
        'template': 'generate-diagram-description.j2',
        'output': 'output/flowchart-analysis.md',
        'filter': '*.py',
        'variables': {
            'diagramType': 'flowchart'
        }
    }
    
    try:
        executor2 = Code2PromptExecutor(config2)
        result2 = executor2.execute()
        print(f"\n✓ Successfully generated flowchart prompt")
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

