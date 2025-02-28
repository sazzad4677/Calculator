# Calculator Program

This is a simple command-line calculator that allows users to perform basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features
- Supports the following operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- Allows continuous calculations using the previous result.
- Validates user input to ensure correct operation selection.
- Ensures the user provides a valid response when choosing to continue or exit.

## How to Use
1. Run the script in a Python environment.
2. Enter the first number when prompted.
3. Enter the second number.
4. Choose an operation (`+`, `-`, `*`, or `/`).
5. View the result.
6. Choose whether to continue with the result (`y`) or exit (`n`).
7. If an invalid input is entered, the program will prompt the user again.

## Example Usage
```
Enter a number: 10
Enter another number: 5
+
-
*
/
Enter your operation: *
10 * 5 = 50.0
Would you like to do another operation? (y/n): y
Enter another number: 2
+
-
*
/
Enter your operation: +
50.0 + 2 = 52.0
Would you like to do another operation? (y/n): n
Thank you for using the calculator!
```

## Requirements
- Python 3.x

## Running the Program
Save the script as `calculator.py` and run it using:
```sh
python calculator.py
```

## License
This project is open-source and free to use.

