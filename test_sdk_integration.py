#!/usr/bin/env python3
"""
Test script to verify the SDK integration.
This demonstrates that the refactored code works with the native Python SDK.
"""

from code2prompt_executor import Code2PromptExecutor
from pathlib import Path


def test_basic_usage():
    """Test basic SDK usage."""
    print("=" * 80)
    print("Test 1: Basic SDK Usage")
    print("=" * 80)
    
    config = {
        'path': '.',
        'filter': '*.py',
        'exclude': '__pycache__/*,*.pyc,test_*.py',
        'line_number': True,
    }
    
    try:
        executor = Code2PromptExecutor(config)
        result = executor.execute()
        
        print(f"\n✓ Successfully generated prompt using SDK")
        print(f"  Length: {len(result)} characters")
        print(f"  First 200 chars: {result[:200]}...")
        return True
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False


def test_with_template():
    """Test SDK with template."""
    print("\n" + "=" * 80)
    print("Test 2: SDK with Template")
    print("=" * 80)
    
    # Check if template exists
    template = Path('generate-diagram-description.j2')
    if not template.exists():
        print(f"⚠ Template not found: {template}")
        print("  Skipping template test")
        return True
    
    config = {
        'path': '.',
        'template': 'generate-diagram-description.j2',
        'output': 'output/sdk-test-output.md',
        'filter': '*.py',
        'exclude': '__pycache__/*,*.pyc',
        'variables': {
            'diagramType': 'uml'
        }
    }
    
    try:
        executor = Code2PromptExecutor(config)
        result = executor.execute()
        
        output_file = Path(config['output'])
        if output_file.exists():
            print(f"\n✓ Successfully generated prompt with template")
            print(f"  Output saved to: {output_file}")
            print(f"  File size: {output_file.stat().st_size} bytes")
            return True
        else:
            print(f"\n✗ Output file not created: {output_file}")
            return False
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False


def test_convenience_method():
    """Test the convenience method."""
    print("\n" + "=" * 80)
    print("Test 3: Convenience Method")
    print("=" * 80)
    
    template = Path('generate-diagram-description.j2')
    if not template.exists():
        print(f"⚠ Template not found: {template}")
        print("  Skipping convenience method test")
        return True
    
    config = {
        'path': '.',
        'filter': '*.py',
        'exclude': '__pycache__/*,*.pyc',
    }
    
    try:
        executor = Code2PromptExecutor(config)
        result = executor.execute_with_template_vars(
            template='generate-diagram-description.j2',
            variables={'diagramType': 'flowchart'},
            output_path='output/sdk-convenience-test.md'
        )
        
        print(f"\n✓ Successfully used convenience method")
        print(f"  Generated {len(result)} characters")
        return True
    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False


def main():
    """Run all tests."""
    print("\n")
    print("╔" + "=" * 78 + "╗")
    print("║" + " " * 20 + "Code2Prompt SDK Integration Tests" + " " * 24 + "║")
    print("╚" + "=" * 78 + "╝")
    print()
    
    results = []
    
    # Run tests
    results.append(("Basic Usage", test_basic_usage()))
    results.append(("With Template", test_with_template()))
    results.append(("Convenience Method", test_convenience_method()))
    
    # Summary
    print("\n" + "=" * 80)
    print("Test Summary")
    print("=" * 80)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  {status}: {test_name}")
    
    print()
    print(f"Results: {passed}/{total} tests passed")
    print("=" * 80)
    
    return 0 if passed == total else 1


if __name__ == '__main__':
    import sys
    sys.exit(main())

