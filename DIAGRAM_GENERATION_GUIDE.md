# Code2Prompt Diagram Generation Guide

This guide shows you how to use `code2prompt` to generate detailed codebase descriptions for AI diagram makers.

## Prerequisites

### Install code2prompt

Choose one of the following installation methods:

```bash
# Option 1: Using Cargo (Rust)
cargo install code2prompt

# Option 2: Using npm
npm install -g code2prompt

# Option 3: Using Homebrew (macOS)
brew install code2prompt
```

Verify installation:
```bash
code2prompt --version
```

## Available Templates

This project includes three templates for different use cases:

### 1. `generate-architecture-diagram.hbs`
- Generates D2 diagram code directly
- Best for: D2 diagram syntax output
- Includes detailed instructions for D2 format

### 2. `generate-diagram-description.hbs`
- Generates comprehensive codebase analysis
- Best for: Detailed architectural documentation
- Includes suggested diagram elements and relationships

### 3. `generate-mermaid-diagram.hbs`
- Generates Mermaid diagram syntax
- Best for: Mermaid-based diagram tools
- Creates class, component, and sequence diagrams

## Usage Commands

### Basic Usage (Current Directory)

```bash
# Using the detailed description template
code2prompt . \
  --template generate-diagram-description.hbs \
  --output-file codebase-description.md

# Using the D2 diagram template
code2prompt . \
  --template generate-architecture-diagram.hbs \
  --output-file d2-diagram-prompt.md

# Using the Mermaid diagram template
code2prompt . \
  --template generate-mermaid-diagram.hbs \
  --output-file mermaid-diagram-prompt.md
```

### Advanced Usage with Filters

#### Include Only Specific File Types

```bash
# Python files only
code2prompt . \
  --include "*.py" \
  --template generate-diagram-description.hbs \
  --output-file python-codebase-description.md

# Multiple file types
code2prompt . \
  --include "*.py,*.js,*.ts" \
  --template generate-diagram-description.hbs \
  --output-file codebase-description.md
```

#### Exclude Directories/Files

```bash
# Exclude common directories
code2prompt . \
  --exclude "node_modules/,__pycache__/,.git/,venv/,dist/" \
  --template generate-diagram-description.hbs \
  --output-file codebase-description.md

# Exclude test files
code2prompt . \
  --exclude "*test*,*spec*" \
  --template generate-diagram-description.hbs \
  --output-file codebase-description.md
```

#### Combined Include and Exclude

```bash
code2prompt . \
  --include "*.py,*.md" \
  --exclude "__pycache__/,*.pyc,venv/" \
  --template generate-diagram-description.hbs \
  --output-file filtered-codebase-description.md
```

### Copy Output to Clipboard

```bash
# macOS
code2prompt . \
  --template generate-mermaid-diagram.hbs | pbcopy

# Linux
code2prompt . \
  --template generate-mermaid-diagram.hbs | xclip -selection clipboard

# Windows (PowerShell)
code2prompt . \
  --template generate-mermaid-diagram.hbs | Set-Clipboard
```

### Generate for Specific Subdirectory

```bash
code2prompt ./src \
  --template generate-diagram-description.hbs \
  --output-file src-architecture.md
```

## Workflow for AI Diagram Maker

### Step 1: Generate the Description

```bash
code2prompt . \
  --include "*.py" \
  --exclude "__pycache__/" \
  --template generate-mermaid-diagram.hbs \
  --output-file diagram-prompt.md
```

### Step 2: Feed to AI Diagram Maker

```bash
# Read the generated file
cat diagram-prompt.md

# Or copy to clipboard and paste into AI Diagram Maker
cat diagram-prompt.md | pbcopy  # macOS
```

### Step 3: Process with AI Diagram Maker

Use the generated description as input to your AI diagram maker tool (e.g., aidiagrammaker, ChatGPT, Claude, etc.).

## Example: Generate Diagram for This Banking System

```bash
# Full detailed analysis
code2prompt /Users/raja/Documents/Raja/projects/diagram-maker/Simple-Banking-System \
  --include "*.py" \
  --exclude "__pycache__/" \
  --template generate-diagram-description.hbs \
  --output-file banking-system-analysis.md

# Generate Mermaid diagram prompt
code2prompt /Users/raja/Documents/Raja/projects/diagram-maker/Simple-Banking-System \
  --include "*.py" \
  --exclude "__pycache__/" \
  --template generate-mermaid-diagram.hbs \
  --output-file banking-system-mermaid.md

# Generate D2 diagram prompt
code2prompt /Users/raja/Documents/Raja/projects/diagram-maker/Simple-Banking-System \
  --include "*.py" \
  --exclude "__pycache__/" \
  --template generate-architecture-diagram.hbs \
  --output-file banking-system-d2.md
```

## Tips and Best Practices

### 1. Filter Wisely
- Always exclude build artifacts, dependencies, and cache directories
- Focus on source code files relevant to architecture
- Use `--include` to limit to specific file types

### 2. Template Selection
- **For AI Tools**: Use `generate-diagram-description.hbs` for most AI tools
- **For D2 Output**: Use `generate-architecture-diagram.hbs` 
- **For Mermaid**: Use `generate-mermaid-diagram.hbs`

### 3. Output Size
- Large codebases generate large outputs
- Consider filtering by directory or file type
- You can use `--line-limit` to limit file content size

### 4. Custom Templates
You can create your own templates using Handlebars syntax. Available variables:
- `{{absolute_code_path}}` - Full path to codebase
- `{{source_tree}}` - Directory tree structure
- `{{files}}` - Array of file objects
- `{{files.path}}` - File path
- `{{files.code}}` - File contents
- `{{files.extension}}` - File extension
- `{{files.lines}}` - Number of lines

## Troubleshooting

### Command not found
```bash
# Check if code2prompt is installed
which code2prompt

# If not found, reinstall
cargo install code2prompt
```

### Permission denied
```bash
# Make sure you have read permissions
ls -la

# Run with appropriate permissions
sudo code2prompt . --template generate-diagram-description.hbs
```

### Output too large
```bash
# Limit by file type
code2prompt . --include "*.py,*.js" --template generate-diagram-description.hbs

# Limit by directory
code2prompt ./src --template generate-diagram-description.hbs
```

## Integration with AI Diagram Makers

### Using with ChatGPT/Claude
1. Generate the description using one of the templates
2. Copy the output
3. Paste into ChatGPT/Claude with: "Based on this codebase analysis, create architecture diagrams"

### Using with aidiagrammaker
```bash
# Generate and pipe directly
code2prompt . --template generate-mermaid-diagram.hbs | aidiagrammaker

# Or save and use
code2prompt . --template generate-mermaid-diagram.hbs -o prompt.md
aidiagrammaker < prompt.md
```

### Using with Online Mermaid Editors
1. Generate Mermaid syntax
2. Copy the Mermaid code blocks
3. Paste into [mermaid.live](https://mermaid.live) or similar tools

## References

- [code2prompt Documentation](https://code2prompt.dev/docs/)
- [code2prompt GitHub](https://github.com/mufeedvh/code2prompt)
- [Handlebars Template Syntax](https://handlebarsjs.com/)
- [Mermaid Diagrams](https://mermaid.js.org/)
- [D2 Diagram Language](https://d2lang.com/)

