# Code2Prompt SDK Quick Reference

## Installation

```bash
# Install the Python SDK
pip install code2prompt_rs

# Or use requirements.txt
pip install -r requirements.txt
```

## Quick Start

### Using the Executor (Recommended)

```python
from code2prompt_executor import Code2PromptExecutor

# Basic usage
config = {
    'path': '.',
    'include_patterns': ['*.py'],
    'exclude_patterns': ['__pycache__/*'],
}

executor = Code2PromptExecutor(config)
prompt = executor.execute()
print(prompt)
```

### Direct SDK Usage

```python
from code2prompt_rs import Code2Prompt

# Simple
c2p = Code2Prompt(path='.')
prompt = c2p.generate_prompt()

# With filters
c2p = Code2Prompt(
    path='.',
    include_patterns=['*.py'],
    exclude_patterns=['__pycache__/*']
)
prompt = c2p.generate_prompt()
```

## Common Patterns

### Pattern 1: Generate Diagram Description

```python
from code2prompt_executor import Code2PromptExecutor

config = {
    'path': '.',
    'template': 'generate-diagram-description.j2',
    'output': 'output/diagram.md',
    'include_patterns': ['*.py'],
    'variables': {'diagramType': 'uml'}
}

executor = Code2PromptExecutor(config)
result = executor.execute()
```

### Pattern 2: Multiple File Types

```python
config = {
    'path': '.',
    'include_patterns': ['*.py', '*.js', '*.ts'],  # Multiple types
    'exclude_patterns': ['node_modules/*', '__pycache__/*', '*.pyc'],
    'line_numbers': True,
}

executor = Code2PromptExecutor(config)
result = executor.execute()
```

### Pattern 3: With Template Variables

```python
executor = Code2PromptExecutor({'path': '.'})

result = executor.execute_with_template_vars(
    template='my-template.hbs',
    variables={
        'projectName': 'MyProject',
        'author': 'John Doe',
        'diagramType': 'sequence'
    },
    output_path='output/result.md'
)
```

### Pattern 4: Different Diagram Types

```python
# UML Diagram
executor.execute_with_template_vars(
    template='generate-diagram-description.j2',
    variables={'diagramType': 'uml'},
    output_path='output/uml.md'
)

# Flowchart
executor.execute_with_template_vars(
    template='generate-diagram-description.j2',
    variables={'diagramType': 'flowchart'},
    output_path='output/flowchart.md'
)

# Sequence Diagram
executor.execute_with_template_vars(
    template='generate-diagram-description.j2',
    variables={'diagramType': 'sequence'},
    output_path='output/sequence.md'
)

# ERD
executor.execute_with_template_vars(
    template='generate-diagram-description.j2',
    variables={'diagramType': 'erd'},
    output_path='output/erd.md'
)
```

## Configuration Options

| Key | Type | Description | Example |
|-----|------|-------------|---------|
| `path` | str | Path to analyze (required) | `'.'` or `'/path/to/project'` |
| `include_patterns` | list | File patterns to include | `['*.py', '*.js']` |
| `exclude_patterns` | list | File patterns to exclude | `['node_modules/*', '*.pyc']` |
| `template` | str | Template file path | `'template.j2'` |
| `output` | str | Output file path | `'output/result.md'` |
| `line_numbers` | bool | Add line numbers | `True` |
| `suppress_comments` | bool | Strip comments | `True` |
| `encoding` | str | File encoding | `'utf-8'` |
| `display_tokens` | bool | Display token count | `True` |
| `variables` | dict | Template variables | `{'key': 'value'}` |

## Filter Patterns

### Include Patterns (include_patterns)

```python
# Single type
'include_patterns': ['*.py']

# Multiple types
'include_patterns': ['*.py', '*.js', '*.ts']

# Specific files
'include_patterns': ['main.py', 'app.py']

# With wildcards
'include_patterns': ['src/**/*.py']
```

### Exclude Patterns (exclude_patterns)

```python
# Common excludes
'exclude_patterns': ['__pycache__/*', '*.pyc', '*.pyo']

# Multiple directories
'exclude_patterns': ['node_modules/*', 'dist/*', 'build/*']

# Test files
'exclude_patterns': ['tests/*', '*_test.py', 'test_*.py']

# Combined
'exclude_patterns': ['__pycache__/*', 'node_modules/*', '*.pyc', 'tests/*']
```

## Error Handling

```python
from code2prompt_executor import Code2PromptExecutor

config = {'path': '.', 'include_patterns': ['*.py']}

try:
    executor = Code2PromptExecutor(config)
    result = executor.execute()
    print(f"✓ Success: {len(result)} characters")
except FileNotFoundError as e:
    print(f"✗ File not found: {e}")
except ValueError as e:
    print(f"✗ Invalid configuration: {e}")
except Exception as e:
    print(f"✗ Error: {e}")
```

## Testing

```bash
# Run the test suite
python test_sdk_integration.py

# Run the example script
python code2prompt_executor.py
```

## Tips & Best Practices

### 1. Always Specify Path
```python
# Good
config = {'path': '.'}

# Bad - will raise ValueError
config = {}
```

### 2. Use Appropriate Filters
```python
# Good - specific filters
'include_patterns': ['*.py', '*.js']

# Less optimal - too broad
'include_patterns': ['*']
```

### 3. Exclude Build Artifacts
```python
# Good - exclude generated files
'exclude_patterns': ['__pycache__/*', 'node_modules/*', 'dist/*', 'build/*', '*.pyc']
```

### 4. Use Templates for Consistency
```python
# Good - reusable template
executor.execute_with_template_vars(
    template='shared-template.j2',
    variables={'project': 'MyApp'}
)
```

### 5. Write Output to Files for Large Results
```python
# Good - write to file
config = {
    'path': '.',
    'output': 'output/result.md'  # Large results
}
```

## Common Issues

### Issue: Module Not Found
```bash
pip install code2prompt_rs
```

### Issue: Template Not Found
```python
# Check if template exists
from pathlib import Path
if not Path('template.j2').exists():
    print("Template not found!")
```

### Issue: Empty Result
```python
# Check your filters
config = {
    'path': '.',
    'include_patterns': ['*.py'],  # Make sure this matches your files
}
```

## Performance Tips

1. **Use specific filters** - Don't process unnecessary files
2. **Exclude large directories** - Skip `node_modules/`, `dist/`, etc.
3. **Write to files** - For large outputs, use `output` parameter
4. **Reuse executor** - Create once, call multiple times with different templates

## Next Steps

- Read the [Migration Guide](SDK_MIGRATION_GUIDE.md) for detailed information
- Check out the [Official Documentation](https://code2prompt.dev/docs/)
- Run `python test_sdk_integration.py` to verify your setup
- Explore [example_usage.py](example_usage.py) for more patterns

---

**Need Help?** Check the [Troubleshooting Section](SDK_MIGRATION_GUIDE.md#troubleshooting) in the Migration Guide.

