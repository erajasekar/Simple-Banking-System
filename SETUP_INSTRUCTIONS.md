# Code2Prompt Programmatic Setup Instructions

This guide will help you set up and use code2prompt programmatically in Python.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup Steps

### 1. Create and Activate Virtual Environment

```bash
# Navigate to your project directory
cd /Users/raja/Documents/Raja/projects/diagram-maker/Simple-Banking-System

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### 2. Install Required Packages

```bash
# Install from requirements.txt
pip install -r requirements.txt

# Or install manually
pip install code2prompt jinja2 rich
```

### 3. Verify Installation

```bash
# Check code2prompt installation
code2prompt --version

# List Python packages
pip list | grep code2prompt
```

## Usage

### Basic CLI Usage

```bash
# Generate prompt with custom template
code2prompt \
  --path . \
  --template generate-diagram-description.j2 \
  --output output/diagram-analysis.md \
  --filter "*.py" \
  --variable diagramType=uml
```

### Programmatic Usage

#### Option 1: Using the provided executor script

```bash
# Make the script executable
chmod +x code2prompt_executor.py

# Run the script
python code2prompt_executor.py
```

#### Option 2: Import and use in your own code

```python
from code2prompt_executor import Code2PromptExecutor

# Configure execution
config = {
    'path': '.',  # Directory to analyze
    'template': 'generate-diagram-description.j2',
    'output': 'output/my-analysis.md',
    'filter': '*.py',  # Only Python files
    'variables': {
        'diagramType': 'uml'  # uml, flowchart, sequence, or erd
    }
}

# Execute
executor = Code2PromptExecutor(config)
result = executor.execute()
print(f"Generated prompt with {len(result)} characters")
```

#### Option 3: Direct subprocess call

```python
import subprocess

cmd = [
    'code2prompt',
    '--path', '.',
    '--template', 'generate-diagram-description.j2',
    '--output', 'output/analysis.md',
    '--variable', 'diagramType=flowchart'
]

result = subprocess.run(cmd, capture_output=True, text=True)
print(result.stdout)
```

## Template Variables

The `generate-diagram-description.j2` template supports the following variable:

- `diagramType`: Type of diagram to generate
  - `uml` - UML Class Diagram
  - `flowchart` - Flowchart Diagram
  - `sequence` - Sequence Diagram
  - `erd` - Entity Relationship Diagram

Example:
```bash
code2prompt --path . \
  --template generate-diagram-description.j2 \
  --variable diagramType=sequence \
  --output output/sequence-diagram-prompt.md
```

## Configuration Options

| Option | Description | Example |
|--------|-------------|---------|
| `path` | Path(s) to analyze | `--path .` or `--path src/` |
| `template` | Jinja2 template file | `--template my-template.j2` |
| `output` | Output file path | `--output result.md` |
| `filter` | Include patterns | `--filter "*.py,*.js"` |
| `exclude` | Exclude patterns | `--exclude "tests/*,*.pyc"` |
| `line-number` | Add line numbers | `--line-number` |
| `suppress-comments` | Remove comments | `--suppress-comments` |
| `variable` | Template variable | `--variable key=value` |
| `tokens` | Show token count | `--tokens` |
| `encoding` | Token encoding | `--encoding cl100k_base` |

## Examples

### Example 1: Generate UML Diagram Prompt

```bash
python code2prompt_executor.py
```

This will generate two outputs:
- `output/diagram-analysis.md` - UML diagram prompt
- `output/flowchart-analysis.md` - Flowchart diagram prompt

### Example 2: Analyze Specific Files

```python
from code2prompt_executor import Code2PromptExecutor

config = {
    'path': ['bank.py', 'client.py', 'main.py'],
    'template': 'generate-diagram-description.j2',
    'output': 'output/banking-system-uml.md',
    'line_number': True,
    'variables': {
        'diagramType': 'uml'
    }
}

executor = Code2PromptExecutor(config)
result = executor.execute()
```

### Example 3: Generate All Diagram Types

```python
from code2prompt_executor import Code2PromptExecutor

diagram_types = ['uml', 'flowchart', 'sequence', 'erd']

for diagram_type in diagram_types:
    config = {
        'path': '.',
        'template': 'generate-diagram-description.j2',
        'output': f'output/{diagram_type}-prompt.md',
        'filter': '*.py',
        'variables': {
            'diagramType': diagram_type
        }
    }
    
    executor = Code2PromptExecutor(config)
    result = executor.execute()
    print(f"✓ Generated {diagram_type} prompt")
```

## Template Syntax Reference

### Handlebars vs Jinja2

| Handlebars | Jinja2 | Description |
|------------|--------|-------------|
| `{{variable}}` | `{{ variable }}` | Variable output |
| `{{#each items}}` | `{% for item in items %}` | Loop start |
| `{{/each}}` | `{% endfor %}` | Loop end |
| `{{#if condition}}` | `{% if condition %}` | Conditional start |
| `{{/if}}` | `{% endif %}` | Conditional end |
| `{{#if (eq a b)}}` | `{% if a == b %}` | Equality check |

### Available Template Variables

- `absolute_code_path` - Absolute path to the analyzed code
- `source_tree` - Directory structure tree
- `files` - Array of file objects with:
  - `path` - Relative file path
  - `code` - File contents
- Custom variables passed via `--variable` flag

## Troubleshooting

### Issue: "command not found: code2prompt"

**Solution**: Ensure the virtual environment is activated and code2prompt is installed:
```bash
source venv/bin/activate
pip install code2prompt
```

### Issue: "Template file not found"

**Solution**: Use absolute paths or ensure you're in the correct directory:
```python
from pathlib import Path

template_path = Path(__file__).parent / 'generate-diagram-description.j2'
config = {'template': str(template_path), ...}
```

### Issue: "No files found"

**Solution**: Check your filter patterns:
```bash
# List what would be included
code2prompt --path . --filter "*.py" --dry-run
```

## Deactivating Virtual Environment

When you're done working:

```bash
deactivate
```

## Additional Resources

- [Code2Prompt Documentation](https://code2prompt.dev/docs/)
- [PyPI Package](https://pypi.org/project/code2prompt/)
- [Jinja2 Template Documentation](https://jinja.palletsprojects.com/)

## Notes

1. The Jinja2 template (`generate-diagram-description.j2`) is a direct conversion from Handlebars (`.hbs`) format
2. All diagram types (uml, flowchart, sequence, erd) are supported via the `diagramType` variable
3. The executor script includes error handling and validation
4. Output files are saved to the `output/` directory by default

