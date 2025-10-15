# Code2Prompt Quick Reference Card

## Installation
```bash
cargo install code2prompt
```

## Quick Commands for This Project

### 1️⃣ Generate Detailed Codebase Analysis
```bash
code2prompt . \
  --include "*.py" \
  --exclude "__pycache__/" \
  --template generate-diagram-description.hbs \
  --output-file output/codebase-analysis.md
```

### 2️⃣ Generate Mermaid Diagram Prompt
```bash
code2prompt . \
  --include "*.py" \
  --exclude "__pycache__/" \
  --template generate-mermaid-diagram.hbs \
  --output-file output/mermaid-prompt.md
```

### 3️⃣ Generate D2 Diagram Prompt
```bash
code2prompt . \
  --include "*.py" \
  --exclude "__pycache__/" \
  --template generate-architecture-diagram.hbs \
  --output-file output/d2-prompt.md
```

### 4️⃣ Copy to Clipboard (macOS)
```bash
code2prompt . \
  --include "*.py" \
  --template generate-mermaid-diagram.hbs | pbcopy
```

## Template Selection Guide

| Template | Use Case | Output Format |
|----------|----------|---------------|
| `generate-diagram-description.hbs` | Comprehensive analysis | Markdown with detailed breakdown |
| `generate-mermaid-diagram.hbs` | Mermaid diagrams | Mermaid syntax ready |
| `generate-architecture-diagram.hbs` | D2 diagrams | D2 syntax ready |

## Common Options

| Option | Description | Example |
|--------|-------------|---------|
| `--include` | File patterns to include | `--include "*.py,*.js"` |
| `--exclude` | File patterns to exclude | `--exclude "__pycache__/,*.pyc"` |
| `--template` | Template file to use | `--template my-template.hbs` |
| `--output-file` | Output file path | `--output-file result.md` |
| `--tokens` | Display token count | `--tokens` |

## Glob Patterns

```bash
# Single extension
--include "*.py"

# Multiple extensions  
--include "*.py,*.js,*.ts"

# Exclude directories
--exclude "node_modules/,venv/,__pycache__/"

# Exclude patterns
--exclude "*test*,*spec*,*.pyc"
```

## One-Liner for AI Diagram Maker

```bash
# Generate and display
code2prompt . --include "*.py" --template generate-mermaid-diagram.hbs

# Generate and save
code2prompt . --include "*.py" --template generate-mermaid-diagram.hbs --output-file diagram-prompt.md

# Generate and copy
code2prompt . --include "*.py" --template generate-mermaid-diagram.hbs | pbcopy
```

## Workflow

```
┌─────────────────────────┐
│  1. Run code2prompt     │
│     with template       │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  2. Generated prompt    │
│     saved to file       │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  3. Copy content to     │
│     AI Diagram Maker    │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  4. Get generated       │
│     diagram output      │
└─────────────────────────┘
```

## Pro Tips

✅ **DO**
- Always exclude cache/build directories
- Filter by relevant file types
- Use descriptive output filenames
- Review generated prompts before using

❌ **DON'T**
- Include node_modules or venv
- Process binary files
- Use without filters on large projects
- Forget to specify output path

## Need Help?

```bash
# Show help
code2prompt --help

# Show version
code2prompt --version

# List available options
code2prompt --help | less
```

