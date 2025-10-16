# Code2Prompt - Programmatic Usage Guide

A complete setup for using code2prompt programmatically to generate AI-ready prompts for diagram generation.

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [What's Included](#whats-included)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Template Customization](#template-customization)
- [Troubleshooting](#troubleshooting)

## 🚀 Quick Start

```bash
# 1. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run examples
python example_usage.py

# 4. Check generated outputs
ls -la output/
```

## 📦 What's Included

| File | Description |
|------|-------------|
| `code2prompt_executor.py` | Main Python class for programmatic execution |
| `generate-diagram-description.j2` | Jinja2 template for diagram generation prompts |
| `example_usage.py` | Comprehensive usage examples |
| `requirements.txt` | Python package dependencies |
| `config.example.json` | Example JSON configuration file |
| `SETUP_INSTRUCTIONS.md` | Detailed setup and usage instructions |

## 💻 Installation

### Step 1: Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (optional)

### Step 2: Virtual Environment Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # macOS/Linux
# OR
venv\Scripts\activate     # Windows
```

### Step 3: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt

# Verify installation
code2prompt --version
python -c "import jinja2; print('Jinja2:', jinja2.__version__)"
```

## 🎯 Usage

### Method 1: Using the Executor Class

```python
from code2prompt_executor import Code2PromptExecutor

config = {
    'path': '.',
    'template': 'generate-diagram-description.j2',
    'output': 'output/my-prompt.md',
    'filter': '*.py',
    'variables': {
        'diagramType': 'uml'  # uml, flowchart, sequence, erd
    }
}

executor = Code2PromptExecutor(config)
result = executor.execute()
print(f"Generated {len(result)} characters")
```

### Method 2: Using JSON Configuration

```python
import json
from code2prompt_executor import Code2PromptExecutor

# Load config from file
with open('config.json', 'r') as f:
    config = json.load(f)

executor = Code2PromptExecutor(config)
result = executor.execute()
```

### Method 3: Direct CLI Usage

```bash
code2prompt \
  --path . \
  --template generate-diagram-description.j2 \
  --output output/result.md \
  --filter "*.py" \
  --variable diagramType=uml
```

## ⚙️ Configuration

### Configuration Options

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `path` | str/list | Path(s) to analyze | `"."` or `["src/", "lib/"]` |
| `template` | str | Jinja2 template file | `"my-template.j2"` |
| `output` | str | Output file path | `"output/result.md"` |
| `filter` | str | Include patterns | `"*.py,*.js"` |
| `exclude` | str | Exclude patterns | `"tests/*,*.pyc"` |
| `line_number` | bool | Add line numbers | `true` |
| `suppress_comments` | bool | Remove comments | `false` |
| `tokens` | bool | Show token count | `true` |
| `encoding` | str | Token encoding | `"cl100k_base"` |
| `variables` | dict | Template variables | `{"diagramType": "uml"}` |

### Diagram Types

The template supports these diagram types via the `diagramType` variable:

- **`uml`** - UML Class Diagram (classes, attributes, methods, relationships)
- **`flowchart`** - Flowchart (processes, decisions, flow)
- **`sequence`** - Sequence Diagram (actors, interactions, messages)
- **`erd`** - Entity Relationship Diagram (entities, attributes, relationships)

### Example Configuration File

```json
{
  "path": ".",
  "template": "generate-diagram-description.j2",
  "output": "output/diagram-prompt.md",
  "filter": "*.py",
  "exclude": "__pycache__/*,venv/*",
  "line_number": true,
  "variables": {
    "diagramType": "uml"
  }
}
```

## 📚 Examples

### Example 1: Single Diagram Type

```python
from code2prompt_executor import Code2PromptExecutor

config = {
    'path': '.',
    'template': 'generate-diagram-description.j2',
    'output': 'output/uml-prompt.md',
    'filter': '*.py',
    'variables': {'diagramType': 'uml'}
}

executor = Code2PromptExecutor(config)
result = executor.execute()
```

### Example 2: Multiple Files

```python
config = {
    'path': ['bank.py', 'client.py', 'main.py'],
    'template': 'generate-diagram-description.j2',
    'output': 'output/specific-files.md',
    'line_number': True,
    'variables': {'diagramType': 'sequence'}
}

executor = Code2PromptExecutor(config)
result = executor.execute()
```

### Example 3: All Diagram Types

```python
from code2prompt_executor import Code2PromptExecutor

diagram_types = ['uml', 'flowchart', 'sequence', 'erd']

for dtype in diagram_types:
    config = {
        'path': '.',
        'template': 'generate-diagram-description.j2',
        'output': f'output/{dtype}-prompt.md',
        'filter': '*.py',
        'variables': {'diagramType': dtype}
    }
    
    executor = Code2PromptExecutor(config)
    executor.execute()
    print(f"✓ Generated {dtype} prompt")
```

### Example 4: With Token Counting

```python
config = {
    'path': '.',
    'template': 'generate-diagram-description.j2',
    'output': 'output/with-tokens.md',
    'filter': '*.py',
    'tokens': True,
    'encoding': 'cl100k_base',  # GPT-4 encoding
    'variables': {'diagramType': 'flowchart'}
}

executor = Code2PromptExecutor(config)
result = executor.execute()
```

### Run All Examples

```bash
python example_usage.py
```

This will generate:
- `output/banking-uml-prompt.md`
- `output/uml-prompt.md`
- `output/flowchart-prompt.md`
- `output/sequence-prompt.md`
- `output/erd-prompt.md`
- `output/core-banking-uml.md`
- `output/sequence-with-tokens.md`
- `output/flowchart-from-config.md`

## 🎨 Template Customization

### Template Structure

The Jinja2 template uses these variables:

```jinja2
{{ absolute_code_path }}  - Absolute path to code
{{ source_tree }}         - Directory tree structure
{{ diagramType }}         - Diagram type (from variables)

{% for file in files %}   - Loop through files
  {{ file.path }}         - File path
  {{ file.code }}         - File contents
{% endfor %}
```

### Creating Custom Templates

1. Create a new `.j2` file:

```jinja2
# My Custom Template

## Project: {{ absolute_code_path }}

### Code Files:

{% for file in files %}
### {{ file.path }}
```
{{ file.code }}
```
{% endfor %}

Custom variable: {{ myCustomVar }}
```

2. Use with custom variables:

```python
config = {
    'path': '.',
    'template': 'my-custom-template.j2',
    'output': 'output/custom.md',
    'variables': {
        'myCustomVar': 'Hello World'
    }
}
```

### Handlebars vs Jinja2 Syntax

| Handlebars | Jinja2 | Usage |
|------------|--------|-------|
| `{{var}}` | `{{ var }}` | Output variable |
| `{{#each items}}` | `{% for item in items %}` | Loop |
| `{{/each}}` | `{% endfor %}` | End loop |
| `{{#if cond}}` | `{% if cond %}` | Conditional |
| `{{/if}}` | `{% endif %}` | End conditional |
| `{{#if (eq a b)}}` | `{% if a == b %}` | Equality |

## 🔧 Troubleshooting

### Issue: "command not found: code2prompt"

**Solution**:
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall code2prompt
pip install --upgrade code2prompt
```

### Issue: "Template file not found"

**Solution**:
```python
from pathlib import Path

# Use absolute path
template = Path(__file__).parent / 'generate-diagram-description.j2'
config = {'template': str(template), ...}
```

### Issue: "No files found"

**Solution**:
```bash
# Test your filter patterns
code2prompt --path . --filter "*.py" --dry-run

# Check what files exist
ls -R *.py
```

### Issue: ModuleNotFoundError

**Solution**:
```bash
# Ensure all dependencies are installed
pip install -r requirements.txt

# Check installed packages
pip list
```

### Issue: "Invalid template syntax"

**Solution**:
- Ensure you're using Jinja2 syntax (`.j2`), not Handlebars (`.hbs`)
- Check for proper `{% %}` and `{{ }}` delimiters
- Validate template syntax: `python -m jinja2 template.j2`

## 🔗 Resources

- [Code2Prompt Documentation](https://code2prompt.dev/docs/)
- [PyPI Package](https://pypi.org/project/code2prompt/)
- [Jinja2 Template Guide](https://jinja.palletsprojects.com/)
- [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md) - Detailed setup guide

## 📝 Best Practices

1. **Always use virtual environments** to isolate dependencies
2. **Test templates** with small codebases first
3. **Use token counting** to ensure LLM compatibility
4. **Leverage filters** to exclude unnecessary files
5. **Version control** your templates and configs
6. **Document custom variables** in your templates

## 🎓 Workflow Integration

### Basic Workflow

```bash
# 1. Activate environment
source venv/bin/activate

# 2. Generate diagram prompt
python -c "
from code2prompt_executor import Code2PromptExecutor
config = {
    'path': '.',
    'template': 'generate-diagram-description.j2',
    'output': 'output/diagram.md',
    'filter': '*.py',
    'variables': {'diagramType': 'uml'}
}
Code2PromptExecutor(config).execute()
"

# 3. Use the generated prompt with your LLM
cat output/diagram.md | llm "Generate a diagram"
```

### Batch Processing

```python
# Process multiple projects
projects = [
    {'name': 'Project A', 'path': '/path/to/project-a'},
    {'name': 'Project B', 'path': '/path/to/project-b'},
]

for project in projects:
    config = {
        'path': project['path'],
        'template': 'generate-diagram-description.j2',
        'output': f"output/{project['name']}-diagram.md",
        'filter': '*.py,*.js',
        'variables': {'diagramType': 'uml'}
    }
    executor = Code2PromptExecutor(config)
    executor.execute()
```

## 🚦 Next Steps

1. ✅ Set up virtual environment
2. ✅ Install dependencies
3. ✅ Run example scripts
4. 📝 Customize templates for your needs
5. 🔄 Integrate into your workflow
6. 🎨 Generate diagrams with your LLM

---

**Happy Coding!** 🎉

For detailed instructions, see [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)

