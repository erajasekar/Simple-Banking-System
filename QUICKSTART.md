# ⚡ Quick Start Guide - Code2Prompt

Get up and running with code2prompt in 3 minutes!

## 🎯 What This Does

Convert your Python code into AI-ready prompts for generating diagrams (UML, flowcharts, sequence, ERD).

## 📦 One-Time Setup (2 minutes)

```bash
# Navigate to project directory
cd /Users/raja/Documents/Raja/projects/diagram-maker/Simple-Banking-System

# Run setup
./run_code2prompt.sh setup
```

This will:
- ✅ Create virtual environment
- ✅ Install code2prompt and dependencies
- ✅ Set up output directory

## 🚀 Quick Usage

### Option 1: Shell Script (Easiest)

```bash
# Generate a single diagram type
./run_code2prompt.sh uml

# Generate all diagram types at once
./run_code2prompt.sh all

# Clean outputs
./run_code2prompt.sh clean
```

### Option 2: Python Script

```bash
# Activate virtual environment
source venv/bin/activate

# Run examples
python example_usage.py
```

### Option 3: Direct Code2Prompt CLI

```bash
# Activate virtual environment
source venv/bin/activate

# Run code2prompt
code2prompt \
  --path . \
  --template generate-diagram-description.j2 \
  --output output/my-diagram.md \
  --filter "*.py" \
  --variable diagramType=uml
```

## 📊 Diagram Types Available

| Type | Command | Description |
|------|---------|-------------|
| UML | `./run_code2prompt.sh uml` | Classes, attributes, methods, relationships |
| Flowchart | `./run_code2prompt.sh flowchart` | Process flow, decisions, loops |
| Sequence | `./run_code2prompt.sh sequence` | Actor interactions, method calls |
| ERD | `./run_code2prompt.sh erd` | Entities, attributes, relationships |

## 📁 Output Files

Generated files are saved in `output/` directory:

```
output/
├── uml-prompt.md          # UML class diagram prompt
├── flowchart-prompt.md    # Flowchart diagram prompt
├── sequence-prompt.md     # Sequence diagram prompt
└── erd-prompt.md          # ERD prompt
```

## 🎓 Next Steps

### Use the Generated Prompts

```bash
# View the generated prompt
cat output/uml-prompt.md

# Copy to clipboard (macOS)
cat output/uml-prompt.md | pbcopy

# Use with an LLM to generate diagrams
# Paste the content into ChatGPT, Claude, etc.
```

### Customize for Your Needs

1. **Edit the template**: Modify `generate-diagram-description.j2`
2. **Adjust filters**: Edit patterns in `run_code2prompt.sh` or `example_usage.py`
3. **Create config file**: Copy `config.example.json` to `config.json` and customize

## 📖 Documentation

- **Quick Reference**: This file
- **Detailed Setup**: [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md)
- **Complete Guide**: [CODE2PROMPT_README.md](CODE2PROMPT_README.md)
- **Official Docs**: https://code2prompt.dev/docs/

## 🔧 Common Commands

```bash
# Setup environment
./run_code2prompt.sh setup

# Generate UML diagram prompt
./run_code2prompt.sh uml

# Generate all diagram types
./run_code2prompt.sh all

# Run Python examples
python example_usage.py

# Clean outputs
./run_code2prompt.sh clean

# View help
./run_code2prompt.sh help
```

## 💡 Pro Tips

1. **Start with UML**: `./run_code2prompt.sh uml` - Best for code structure
2. **Use filters**: Exclude test files and generated code
3. **Check token count**: Add `--tokens` flag to see prompt size
4. **Iterate quickly**: Modify template → regenerate → test with LLM

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| Command not found | Run `./run_code2prompt.sh setup` first |
| Permission denied | Run `chmod +x run_code2prompt.sh` |
| No files generated | Check `--filter` patterns match your files |
| Template error | Ensure using `.j2` (Jinja2) not `.hbs` |

## 🎯 Typical Workflow

```bash
# 1. Setup (first time only)
./run_code2prompt.sh setup

# 2. Generate diagram prompt
./run_code2prompt.sh uml

# 3. View the output
cat output/uml-prompt.md

# 4. Copy and paste into your LLM
# ChatGPT, Claude, etc.

# 5. LLM generates the diagram code
# (Mermaid, PlantUML, etc.)

# 6. Visualize the diagram
# Use online tools or extensions
```

## 🔄 Regular Usage

After initial setup, just run:

```bash
# Activate environment
source venv/bin/activate

# Generate what you need
./run_code2prompt.sh all

# Done!
```

## 📚 Files Created

- ✅ `code2prompt_executor.py` - Main executor class
- ✅ `generate-diagram-description.j2` - Jinja2 template
- ✅ `example_usage.py` - Usage examples
- ✅ `run_code2prompt.sh` - Quick run script
- ✅ `requirements.txt` - Dependencies
- ✅ `config.example.json` - Config template
- ✅ Documentation files

## 🎉 You're Ready!

Start generating diagram prompts:

```bash
./run_code2prompt.sh all
```

Then use the generated prompts with your favorite LLM to create beautiful diagrams! 🎨

---

**Need Help?** Check [CODE2PROMPT_README.md](CODE2PROMPT_README.md) for detailed documentation.

