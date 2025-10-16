# Code2Prompt SDK Migration Guide

## Overview

We've migrated from using the Code2Prompt CLI via subprocess to using the native Python SDK (`code2prompt_rs`). This provides better performance, error handling, and a more Pythonic interface.

## What Changed

### Before (Subprocess Approach)
```python
# Old: Used subprocess to call CLI
import subprocess

result = subprocess.run(
    ['code2prompt', '--path', '.', '--filter', '*.py'],
    capture_output=True,
    text=True
)
```

### After (Native SDK Approach)
```python
# New: Direct Python SDK usage
from code2prompt_rs import Code2Prompt

c2p = Code2Prompt(
    path='.',
    include_patterns=['*.py']
)
prompt = c2p.generate_prompt()
```

## Installation

### 1. Uninstall CLI (Optional)
```bash
pip uninstall code2prompt
```

### 2. Install SDK
```bash
pip install code2prompt_rs
```

Or use the updated requirements file:
```bash
pip install -r requirements.txt
```

## API Changes

The `Code2PromptExecutor` API remains **exactly the same**! Your existing code doesn't need to change.

### Configuration Mapping

Under the hood, these mappings are now applied:

| Old Config Key | SDK Parameter | Type | Example |
|---------------|---------------|------|---------|
| `path` | `path` | string | `'.'` |
| `filter` | `include_patterns` | list | `['*.py', '*.js']` |
| `exclude` | `exclude_patterns` | list | `['__pycache__/*']` |
| `template` | `template_path` | string | `'template.j2'` |
| `line_number` | `line_numbers` | bool | `True` |
| `suppress_comments` | `suppress_comments` | bool | `True` |
| `encoding` | `encoding` | string | `'utf-8'` |
| `variables` | `template_variables` | dict | `{'key': 'value'}` |
| `tokens` | `display_tokens` | bool | `True` |

## Usage Examples

### Example 1: Basic Usage (Unchanged)
```python
from code2prompt_executor import Code2PromptExecutor

config = {
    'path': '.',
    'filter': '*.py',
    'exclude': '__pycache__/*,*.pyc',
    'line_number': True,
}

executor = Code2PromptExecutor(config)
result = executor.execute()
print(result)
```

### Example 2: With Template (Unchanged)
```python
config = {
    'path': '.',
    'template': 'generate-diagram-description.j2',
    'output': 'output/diagram-analysis.md',
    'filter': '*.py',
    'variables': {
        'diagramType': 'uml'
    }
}

executor = Code2PromptExecutor(config)
result = executor.execute()
```

### Example 3: Using Convenience Method (Unchanged)
```python
executor = Code2PromptExecutor({'path': '.', 'filter': '*.py'})

result = executor.execute_with_template_vars(
    template_path='generate-diagram-description.j2',
    variables={'diagramType': 'flowchart'},
    output_path='output/flowchart.md'
)
```

### Example 4: Direct SDK Usage (New Capability)
```python
from code2prompt_rs import Code2Prompt

# Simple usage
c2p = Code2Prompt(path='.')
prompt = c2p.generate_prompt()

# With filters
c2p = Code2Prompt(
    path='.',
    include_patterns=['*.py', '*.js'],
    exclude_patterns=['__pycache__/*', 'node_modules/*']
)
prompt = c2p.generate_prompt()

# With template
c2p = Code2Prompt(
    path='.',
    template_path='my_template.hbs',
    template_variables={'key': 'value'}
)
prompt = c2p.generate_prompt()
```

## Benefits of SDK Migration

### 1. Performance
- ✅ No subprocess overhead
- ✅ Faster execution
- ✅ Lower memory usage

### 2. Error Handling
- ✅ Native Python exceptions
- ✅ Better stack traces
- ✅ Easier debugging

### 3. Developer Experience
- ✅ Type hints and IDE support
- ✅ Direct API access
- ✅ Pythonic interface

### 4. Integration
- ✅ Seamless integration with Python code
- ✅ Better testability
- ✅ No shell command parsing

## Testing the Migration

Run the test script to verify everything works:

```bash
python test_sdk_integration.py
```

This will run three tests:
1. Basic SDK usage
2. SDK with template
3. Convenience method

## Troubleshooting

### Issue: ImportError: No module named 'code2prompt_rs'

**Solution:**
```bash
pip install code2prompt_rs
```

### Issue: Template not working

**Cause:** The SDK may have different template syntax requirements.

**Solution:** Verify your template is compatible with Handlebars format. The SDK supports both Handlebars (.hbs) and Jinja2 (.j2) templates.

### Issue: Different output than CLI

**Cause:** The SDK may have different defaults or behavior.

**Solution:** Check the SDK documentation and ensure all parameters are correctly mapped. You can add debug logging to see the exact parameters being passed:

```python
sdk_params = executor._convert_config_to_sdk_params()
print(f"SDK Parameters: {sdk_params}")
```

## Rollback Plan

If you need to rollback to the subprocess approach:

1. Checkout the previous version of `code2prompt_executor.py`
2. Reinstall CLI version:
   ```bash
   pip uninstall code2prompt_rs
   pip install code2prompt>=0.8.1
   ```

## Further Reading

- [Code2Prompt Documentation](https://code2prompt.dev/docs/tutorials/getting_started/)
- [SDK API Reference](https://code2prompt.dev/docs/sdk/)
- [Template Documentation](https://code2prompt.dev/docs/tutorials/learn_templating/)

## Questions?

If you encounter any issues or have questions about the migration, please:
1. Check the test script output
2. Review the SDK documentation
3. Verify your Python version (3.8+ required)
4. Check that all dependencies are installed

## Summary

✅ No changes to your existing code  
✅ Better performance and error handling  
✅ Native Python integration  
✅ Same API, better implementation  

The migration is complete and backward compatible!

