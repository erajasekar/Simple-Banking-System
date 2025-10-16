#!/bin/bash

# Code2Prompt Execution Script
# Quick script to run code2prompt with predefined configurations

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Function to print colored output
print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Function to check if virtual environment exists
check_venv() {
    if [ ! -d "venv" ]; then
        print_error "Virtual environment not found!"
        print_info "Creating virtual environment..."
        python3 -m venv venv
        print_success "Virtual environment created"
    fi
}

# Function to activate virtual environment
activate_venv() {
    print_info "Activating virtual environment..."
    source venv/bin/activate
    print_success "Virtual environment activated"
}

# Function to install dependencies
install_deps() {
    print_info "Checking dependencies..."
    
    if ! pip show code2prompt > /dev/null 2>&1; then
        print_warning "Installing dependencies..."
        pip install -q -r requirements.txt
        print_success "Dependencies installed"
    else
        print_success "Dependencies already installed"
    fi
}

# Function to create output directory
ensure_output_dir() {
    mkdir -p output
}

# Function to generate diagram prompt
generate_prompt() {
    local diagram_type=$1
    local output_file="output/${diagram_type}-prompt.md"
    
    print_info "Generating ${diagram_type} diagram prompt..."
    
    code2prompt \
        --path . \
        --template generate-diagram-description.j2 \
        --output "$output_file" \
        --filter "*.py" \
        --exclude "__pycache__/*,venv/*,*.pyc,*_executor.py,example_*.py,run_*.py" \
        --variable "diagramType=${diagram_type}" \
        --line-number
    
    if [ -f "$output_file" ]; then
        local size=$(wc -c < "$output_file")
        print_success "${diagram_type} prompt generated → ${output_file} (${size} bytes)"
    else
        print_error "Failed to generate ${diagram_type} prompt"
        return 1
    fi
}

# Function to display usage
usage() {
    cat << EOF

${GREEN}Code2Prompt Execution Script${NC}

Usage: ./run_code2prompt.sh [OPTION]

Options:
    uml         Generate UML class diagram prompt
    flowchart   Generate flowchart diagram prompt
    sequence    Generate sequence diagram prompt
    erd         Generate entity relationship diagram prompt
    all         Generate all diagram types
    setup       Setup environment (create venv, install deps)
    clean       Clean generated outputs
    help        Display this help message

Examples:
    ./run_code2prompt.sh uml
    ./run_code2prompt.sh all
    ./run_code2prompt.sh setup

EOF
}

# Function to setup environment
setup_environment() {
    echo ""
    echo "=================================="
    echo "  Code2Prompt Environment Setup"
    echo "=================================="
    echo ""
    
    check_venv
    activate_venv
    install_deps
    ensure_output_dir
    
    echo ""
    print_success "Environment setup complete!"
    echo ""
    print_info "You can now run:"
    echo "  ./run_code2prompt.sh uml"
    echo "  ./run_code2prompt.sh all"
    echo "  python example_usage.py"
    echo ""
}

# Function to clean outputs
clean_outputs() {
    print_info "Cleaning generated outputs..."
    
    if [ -d "output" ]; then
        rm -f output/*-prompt.md
        print_success "Cleaned output directory"
    fi
    
    if [ -f "config.json" ]; then
        rm -f config.json
        print_success "Removed generated config.json"
    fi
}

# Main execution
main() {
    local action=${1:-help}
    
    case $action in
        setup)
            setup_environment
            ;;
        
        uml|flowchart|sequence|erd)
            check_venv
            activate_venv
            install_deps
            ensure_output_dir
            echo ""
            generate_prompt "$action"
            echo ""
            ;;
        
        all)
            check_venv
            activate_venv
            install_deps
            ensure_output_dir
            echo ""
            echo "=================================="
            echo "  Generating All Diagram Types"
            echo "=================================="
            echo ""
            
            for dtype in uml flowchart sequence erd; do
                generate_prompt "$dtype"
            done
            
            echo ""
            print_success "All diagram prompts generated!"
            echo ""
            print_info "Generated files:"
            ls -lh output/*-prompt.md 2>/dev/null || true
            echo ""
            ;;
        
        clean)
            clean_outputs
            ;;
        
        help|--help|-h)
            usage
            ;;
        
        *)
            print_error "Unknown option: $action"
            usage
            exit 1
            ;;
    esac
}

# Run main function
main "$@"

