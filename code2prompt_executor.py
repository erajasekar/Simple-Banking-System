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

# link to source https://github.com/mufeedvh/code2prompt/blob/main/crates/code2prompt-python/python-sdk/code2prompt_rs/code2prompt.py
class Code2PromptExecutor:
    """Execute code2prompt programmatically with custom configuration using the Python SDK."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the Code2Prompt executor.
        
        Args:
            config: Configuration dictionary with options like:
                - path: Path to analyze (required)
                - template: Path to Handlebars template file (.hbs)
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
            
            print(f"Executing Code2Prompt SDK with path: {sdk_params.get('path')}")
            if sdk_params.get('include_patterns'):
                print(f"  Include patterns: {sdk_params.get('include_patterns')}")
            if sdk_params.get('exclude_patterns'):
                print(f"  Exclude patterns: {sdk_params.get('exclude_patterns')}")
            if self.config.get('template'):
                print(f"  Template: {self.config.get('template')}")
            
            # Create Code2Prompt instance with SDK parameters
            c2p = Code2Prompt(**sdk_params)
            
            # Generate the prompt using the SDK
            # The generate() method returns a RenderedPrompt object with .prompt attribute
            if self.config.get('template'):
                template_path = Path(self.config['template'])
                
                # Read the template content as a string (SDK expects template content, not path)
                template_content = template_path.read_text(encoding='utf-8')
                
                # Generate with template content
                rendered = c2p.generate(template=template_content)
                prompt_text = rendered.prompt
            else:
                rendered = c2p.generate()
                prompt_text = rendered.prompt
            
            # If output file is specified, write to file
            if self.config.get('output'):
                output_file = Path(self.config['output'])
                output_file.parent.mkdir(parents=True, exist_ok=True)
                output_file.write_text(prompt_text, encoding='utf-8')
                print(f"  Output written to: {output_file}")
            
            return prompt_text
                
        except Exception as e:
            print(f"Error executing code2prompt SDK: {e}")
            raise
    
    def execute_with_template(self, template: str, output_path: Optional[str] = None) -> str:
        """
        Execute code2prompt with a specific template.
        
        Args:
            template: Path to the Handlebars template file (.hbs)
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
        'template': 'generate-diagram-description-flowchart.hbs',
        'output': 'output/flowchart-analysis.md',
        'filter': 'main.py,bank.py,client.py'
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

