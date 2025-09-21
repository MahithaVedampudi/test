import os, sys

def add_numbers(a, b):
  return a + b   # Wrong indentation (2 spaces instead of 4)

def divide(a, b):
    return a / b   # ⚠️ No error handling for divide-by-zero

def main():
    x = 10
    y = 0
    print("Sum:", add_numbers(x, y))
    print("Division:", divide(x, y))  # ⚠️ This will crash if y=0

main()
