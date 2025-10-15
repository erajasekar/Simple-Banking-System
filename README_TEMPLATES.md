# Code2Prompt Templates for AI Diagram Generation

## 📋 Overview

This directory contains three optimized Handlebars templates for generating detailed codebase descriptions that can be used as input for AI diagram makers like **aidiagrammaker**, **ChatGPT**, **Claude**, or other AI tools.

## ✅ What's Included

### 🎨 Templates

1. **`generate-mermaid-diagram.hbs`**
   - Generates prompts for Mermaid diagram syntax
   - Perfect for creating class, component, and sequence diagrams
   - Best for: Mermaid.js, mermaid.live, or AI tools that output Mermaid

2. **`generate-architecture-diagram.hbs`**
   - Generates prompts for D2 diagram syntax
   - Focuses on system architecture visualization
   - Best for: D2 diagrams, architectural documentation

3. **`generate-diagram-description.hbs`**
   - Generates comprehensive codebase analysis
   - Includes detailed breakdown of components and relationships
   - Best for: General-purpose AI diagram generation

### 📚 Documentation

1. **`DIAGRAM_GENERATION_GUIDE.md`** - Complete guide with detailed instructions
2. **`QUICK_REFERENCE.md`** - Quick reference card for common commands
3. **`README_TEMPLATES.md`** - This file

### 📁 Sample Outputs

The `output/` directory contains example generated prompts:
- `mermaid-prompt.md` - Mermaid diagram generation prompt
- `d2-prompt.md` - D2 diagram generation prompt
- `detailed-analysis.md` - Comprehensive codebase analysis

## 🚀 Quick Start

### 1. Install code2prompt

```bash
# Using Cargo (recommended)
cargo install code2prompt

# Or using npm
npm install -g code2prompt
```

### 2. Generate Diagram Prompts

#### For Mermaid Diagrams:
```bash
code2prompt . \
  --include "*.py" \
  --exclude "__pycache__/" \
  --template generate-mermaid-diagram.hbs \
  --output-file output/mermaid-prompt.md
```

#### For D2 Diagrams:
```bash
code2prompt . \
  --include "*.py" \
  --exclude "__pycache__/" \
  --template generate-architecture-diagram.hbs \
  --output-file output/d2-prompt.md
```

#### For Detailed Analysis:
```bash
code2prompt . \
  --include "*.py" \
  --exclude "__pycache__/" \
  --template generate-diagram-description.hbs \
  --output-file output/detailed-analysis.md
```

### 3. Use with AI Diagram Maker

After generating the prompt file:

1. **Copy the content:**
   ```bash
   cat output/mermaid-prompt.md | pbcopy  # macOS
   ```

2. **Paste into your AI tool:**
   - ChatGPT
   - Claude
   - aidiagrammaker
   - Any other AI diagram tool

3. **Get your diagram!** The AI will analyze the code and generate appropriate diagrams.

## 📊 What Each Template Produces

### Mermaid Template Output
Produces a prompt that instructs the AI to create:
- **Class Diagrams** - Classes, attributes, methods, and relationships
- **Component Diagrams** - High-level module dependencies
- **Sequence Diagrams** - User interaction flows

### D2 Template Output
Produces a prompt that instructs the AI to create:
- **Architecture Diagrams** - System layers and components
- **Component Relationships** - Module interactions
- **Data Flow** - How data moves through the system

### Detailed Analysis Template Output
Produces a comprehensive analysis including:
- Complete source code of all files
- Suggested diagram elements
- Architectural patterns identified
- Relationship mappings
- Layered architecture breakdown

## 🎯 Use Cases

### For Software Documentation
```bash
code2prompt . --template generate-diagram-description.hbs \
  --output-file docs/architecture-analysis.md
```

### For Code Reviews
```bash
code2prompt ./src --template generate-mermaid-diagram.hbs \
  --output-file review/component-diagram-prompt.md
```

### For Onboarding New Developers
```bash
code2prompt . --include "*.py,*.js,*.ts" \
  --template generate-architecture-diagram.hbs \
  --output-file onboarding/system-overview-prompt.md
```

### For Technical Presentations
```bash
code2prompt ./core --template generate-mermaid-diagram.hbs | pbcopy
# Then paste into ChatGPT/Claude for instant diagrams
```

## 🔧 Customization

### Filtering Files

```bash
# Only Python files
--include "*.py"

# Multiple file types
--include "*.py,*.js,*.ts"

# Exclude directories
--exclude "node_modules/,__pycache__/,venv/,dist/"

# Exclude test files
--exclude "*test*,*spec*"
```

### Custom Paths

```bash
# Analyze specific directory
code2prompt ./src/core --template generate-mermaid-diagram.hbs

# Analyze multiple related directories
code2prompt ./api --template generate-diagram-description.hbs
code2prompt ./models --template generate-diagram-description.hbs
```

## 💡 Pro Tips

### 1. Start with Mermaid
Mermaid diagrams are widely supported and easy to render. Start with the Mermaid template for quick results.

### 2. Use Filters Aggressively
Always exclude irrelevant directories to keep prompts focused:
```bash
--exclude "__pycache__/,venv/,node_modules/,dist/,build/"
```

### 3. Generate Multiple Perspectives
Run all three templates to get different views of your architecture:
```bash
# Run all three
for template in generate-mermaid-diagram generate-architecture-diagram generate-diagram-description; do
  code2prompt . --include "*.py" --template ${template}.hbs \
    --output-file output/${template%-*}-output.md
done
```

### 4. Version Control Your Prompts
Keep generated prompts in version control to track architectural changes over time:
```bash
git add output/*.md
git commit -m "docs: update architecture diagrams for v2.0"
```

### 5. Combine with CI/CD
Generate architecture documentation automatically in your CI pipeline:
```bash
# .github/workflows/docs.yml
- name: Generate Architecture Docs
  run: |
    code2prompt . --template generate-diagram-description.hbs \
      --output-file docs/architecture.md
```

## 📖 Template Comparison

| Feature | Mermaid | D2 | Detailed Analysis |
|---------|---------|-----|-------------------|
| **Output Type** | Diagram Syntax | Diagram Syntax | Prose + Analysis |
| **Best For** | Quick diagrams | Architecture | Documentation |
| **AI Friendliness** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Detail Level** | Medium | High | Very High |
| **Token Usage** | ~1,000 | ~1,200 | ~1,400 |
| **Learning Curve** | Easy | Medium | Easy |

## 🌐 Supported AI Tools

These templates work with:
- ✅ **ChatGPT** (GPT-4, GPT-3.5)
- ✅ **Claude** (All versions)
- ✅ **aidiagrammaker**
- ✅ **GitHub Copilot Chat**
- ✅ **Any AI with code understanding**

## 🔗 Useful Links

- [code2prompt Documentation](https://code2prompt.dev/docs/)
- [code2prompt GitHub](https://github.com/mufeedvh/code2prompt)
- [Mermaid Live Editor](https://mermaid.live)
- [D2 Language Reference](https://d2lang.com/)
- [Handlebars Templates](https://handlebarsjs.com/)

## 🐛 Troubleshooting

### "Command not found: code2prompt"
```bash
# Reinstall
cargo install code2prompt
# Or
npm install -g code2prompt
```

### "Template rendering error"
- Ensure template file exists
- Check template syntax
- Verify code2prompt version is up to date

### "Output file too large"
```bash
# Use more aggressive filtering
--exclude "*test*,*spec*,__pycache__/,node_modules/"

# Or limit to specific directory
code2prompt ./src/core --template generate-mermaid-diagram.hbs
```

### "AI generates incorrect diagrams"
- Try a different template (Detailed Analysis is most comprehensive)
- Add more context manually after generating
- Split large codebases into smaller sections

## 📝 Example Workflow

1. **Analyze your codebase:**
   ```bash
   code2prompt . --include "*.py" --template generate-mermaid-diagram.hbs \
     --output-file output/analysis.md
   ```

2. **Review the output:**
   ```bash
   cat output/analysis.md
   ```

3. **Feed to AI:**
   Copy content and paste into ChatGPT/Claude with:
   "Please analyze this code and create the requested diagrams"

4. **Save the diagrams:**
   The AI will generate Mermaid/D2 code that you can render or save

5. **Iterate if needed:**
   Refine the prompt or try a different template

## 🎓 Learning Resources

1. Read `DIAGRAM_GENERATION_GUIDE.md` for comprehensive instructions
2. Check `QUICK_REFERENCE.md` for command cheatsheet
3. Examine the sample outputs in the `output/` directory
4. Experiment with different templates on your codebase

## 📄 License

These templates are provided as-is for use with code2prompt. Modify them as needed for your projects.

## 🤝 Contributing

Found a way to improve these templates? Contributions welcome!

---

**Happy Diagramming! 🎨📊**

