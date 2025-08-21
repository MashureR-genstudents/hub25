#!/usr/bin/env python3
"""
Main Python script for local25 repository
"""

def hello_world():
    """Print a hello message"""
    print("Hello from local25 repository!")
    return "Hello World!"

def add_numbers(a, b):
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    hello_world()
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
