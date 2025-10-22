#!/bin/bash

# ============================================
# Code2Prompt Commands for AI Diagram Generation
# ============================================
# Ready-to-use commands for your Simple Banking System
# Just copy and paste these commands into your terminal

# Navigate to project directory
cd /Users/raja/Documents/Raja/projects/diagram-maker/Simple-Banking-System

# ============================================
# BASIC COMMANDS
# ============================================

# 1. Generate Mermaid Diagram Prompt (RECOMMENDED)
echo "🎨 Generating Mermaid diagram prompt..."
code2prompt . \
  --include "*.py" \
  --exclude "__pycache__/" \
  --template generate-mermaid-diagram.hbs \
  --output-file output/mermaid-prompt.md

# 2. Generate D2 Architecture Diagram Prompt
echo "🏗️ Generating D2 diagram prompt..."
code2prompt . \
  --include "*.py" \
  --exclude "__pycache__/" \
  --template generate-architecture-diagram.hbs \
  --output-file output/d2-prompt.md

# 3. Generate Detailed Codebase Analysis
echo "📊 Generating detailed analysis..."
code2prompt . \
  --include "*.py" \
  --exclude "__pycache__/" \
  --template generate-diagram-description.hbs \
  --output-file output/detailed-analysis.md

echo "✅ All prompts generated successfully!"
echo "📁 Check the output/ directory for results"


# Generate flowchart diagram prompt
code2prompt . \
  --include "bank.py, client.py, main.py" \
  --exclude "__pycache__/" \
  --template generate-diagram-description-flowchart.hbs \
  --output-file output/flowchart-analysis.md

# Generate sequence diagram prompt  
code2prompt . \
  --include "bank.py, client.py, main.py" \
  --exclude "__pycache__/" \
  --template generate-diagram-description-sequence.hbs \
  --output-file output/sequence-analysis.md

# Generate UML class diagram prompt
code2prompt . \
  --include "bank.py, client.py, main.py" \
  --exclude "__pycache__/" \
  --template generate-diagram-description-uml.hbs \
  --output-file output/uml-analysis.md

# Generate ERD diagram prompt
code2prompt . \
  --include "bank.py, client.py, main.py" \
  --exclude "__pycache__/" \
  --template generate-diagram-description-erd.hbs \
  --output-file output/erd-analysis.md

# Generate system architecture diagram prompt
code2prompt . \
  --include "bank.py, client.py, main.py" \
  --exclude "__pycache__/" \
  --template generate-diagram-description-system-architecture.hbs \
  --output-file output/system-architecture-analysis.md

# Generate network architecture diagram prompt  
code2prompt . \
  --include "bank.py, client.py, main.py" \
  --exclude "__pycache__/" \
  --template generate-diagram-description-network-architecture.hbs \
  --output-file output/network-architecture-analysis.md



# ============================================
# COPY TO CLIPBOARD (macOS)
# ============================================

# Copy Mermaid prompt to clipboard
# code2prompt . --include "*.py" --exclude "__pycache__/" --template generate-mermaid-diagram.hbs | pbcopy

# Copy D2 prompt to clipboard
# code2prompt . --include "*.py" --exclude "__pycache__/" --template generate-architecture-diagram.hbs | pbcopy

# Copy detailed analysis to clipboard
# code2prompt . --include "*.py" --exclude "__pycache__/" --template generate-diagram-description.hbs | pbcopy

# ============================================
# DISPLAY OUTPUT (View results in terminal)
# ============================================

# View Mermaid prompt
# cat output/mermaid-prompt.md

# View D2 prompt
# cat output/d2-prompt.md

# View detailed analysis
# cat output/detailed-analysis.md

# ============================================
# ADVANCED USAGE
# ============================================

# Include README in analysis
# code2prompt . --include "*.py,*.md" --exclude "__pycache__/" --template generate-diagram-description.hbs --output-file output/full-analysis.md

# Analyze specific file only
# code2prompt . --include "main.py" --template generate-mermaid-diagram.hbs --output-file output/main-only.md

# Generate for subdirectory
# code2prompt ./src --include "*.py" --template generate-mermaid-diagram.hbs --output-file output/src-analysis.md

# ============================================
# WORKFLOW FOR AI DIAGRAM MAKER
# ============================================

# Step 1: Generate prompt
# code2prompt . --include "*.py" --template generate-mermaid-diagram.hbs --output-file output/diagram-prompt.md

# Step 2: Copy to clipboard (macOS)
# cat output/diagram-prompt.md | pbcopy

# Step 3: Paste into AI tool (ChatGPT, Claude, aidiagrammaker, etc.)

# Step 4: Get your diagrams!

echo ""
echo "=========================================="
echo "Next Steps:"
echo "=========================================="
echo "1. Check the output/ directory"
echo "2. Open any generated .md file"
echo "3. Copy the content"
echo "4. Paste into your AI diagram maker"
echo "5. Get beautiful diagrams!"
echo ""
echo "📖 For more info, read DIAGRAM_GENERATION_GUIDE.md"
echo "⚡ For quick reference, read QUICK_REFERENCE.md"
echo ""

