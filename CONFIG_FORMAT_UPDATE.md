# Configuration Format Update

## Overview

The configuration format has been updated to match the SDK's expected parameters directly, eliminating the need for format conversion.

## What Changed

### Old Format (Deprecated)
```python
config = {
    'path': '.',
    'filter': '*.py,*.js',              # ❌ OLD
    'exclude': '__pycache__/*,*.pyc',   # ❌ OLD
    'line_number': True,                # ❌ OLD
    'tokens': True,                     # ❌ OLD
}
```

### New Format (Current)
```python
config = {
    'path': '.',
    'include_patterns': ['*.py', '*.js'],           # ✅ NEW
    'exclude_patterns': ['__pycache__/*', '*.pyc'], # ✅ NEW
    'line_numbers': True,                           # ✅ NEW
    'display_tokens': True,                         # ✅ NEW
}
```

## Migration Guide

### Configuration Key Mapping

| Old Key | New Key | Notes |
|---------|---------|-------|
| `filter` | `include_patterns` | Now expects an array of strings |
| `exclude` | `exclude_patterns` | Now expects an array of strings |
| `line_number` | `line_numbers` | Changed to plural |
| `tokens` | `display_tokens` | More descriptive name |

### Unchanged Keys

These keys remain the same:
- `path` - Path to analyze
- `template` - Template file path
- `output` - Output file path
- `suppress_comments` - Boolean flag
- `encoding` - File encoding

## Benefits

1. **No conversion overhead** - Config maps directly to SDK parameters
2. **Clearer semantics** - Arrays for patterns are more explicit
3. **Better IDE support** - Type hints work better with arrays
4. **Reduced complexity** - No internal format conversion needed

## Quick Migration

If you have existing config files or code using the old format:

1. **Rename keys:**
   - `filter` → `include_patterns`
   - `exclude` → `exclude_patterns`
   - `line_number` → `line_numbers`
   - `tokens` → `display_tokens`

2. **Convert comma-separated strings to arrays:**
   ```python
   # Old
   'filter': '*.py,*.js,*.ts'
   
   # New
   'include_patterns': ['*.py', '*.js', '*.ts']
   ```

3. **Update JSON config files:**
   ```json
   {
     "include_patterns": ["*.py"],
     "exclude_patterns": ["__pycache__/*", "*.pyc"],
     "line_numbers": true,
     "display_tokens": false
   }
   ```

## Examples

### Example 1: Basic Configuration
```python
from code2prompt_executor import Code2PromptExecutor

config = {
    'path': '.',
    'include_patterns': ['*.py'],
    'line_numbers': True
}

executor = Code2PromptExecutor(config)
result = executor.execute()
```

### Example 2: With Templates
```python
config = {
    'path': '.',
    'template': 'generate-diagram-description-flowchart.hbs',
    'output': 'output/flowchart.md',
    'include_patterns': ['main.py', 'bank.py', 'client.py']
}

executor = Code2PromptExecutor(config)
result = executor.execute()
```

### Example 3: Multiple Patterns
```python
config = {
    'path': '.',
    'include_patterns': ['*.py', '*.js', '*.ts'],
    'exclude_patterns': [
        '__pycache__/*',
        'venv/*',
        '*.pyc',
        'node_modules/*'
    ],
    'line_numbers': True,
    'display_tokens': True
}
```

## Files Updated

The following files have been updated to use the new format:
- ✅ `config.example.json`
- ✅ `code2prompt_executor.py`
- ✅ `test_sdk_integration.py`
- ✅ `example_usage.py`

## Backward Compatibility

⚠️ **Breaking Change:** The old config format is no longer supported. You must update your configuration files to use the new format.

## Need Help?

See these files for more examples:
- `config.example.json` - Example configuration file
- `example_usage.py` - Complete usage examples
- `test_sdk_integration.py` - Test examples

---

*Last Updated: October 22, 2025*

