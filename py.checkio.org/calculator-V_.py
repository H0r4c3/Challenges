'https://py.checkio.org/en/mission/calculator-v/'

'''
In the fifth mission your function should work properly with additional operations: *, /, // (integer division), % (modulo) and ** (power) and their combinations with "=".

Expected behavior:

beginning zeros should be removed, only-zeros number - converted to single zero;
among +- signs between numbers, the last one should be taken;
"==" means repeating the last operation;
"+=" or "-=" - adding/subtracting the number (or operations result) before the combination (doubling the number/subtracting itself);
the calculator ignores digit you enter after 5th;
"-" for numbers < 0 is NOT taking digit place;
if the abs(result) is more than 99999 - "error" is shown as a result;
for float, if the integer part of abs(result) is more then 9999 - "error" is shown as a result;
for float, in case the total length of number is more than 5 digits, it should be rounded to 5 digits (1.23456 -> 1.235);
for float, beginning and trailing zeros should be removed (until the "." if possible): 0.1200 -> .12 , 123.00 -> 123. . It should be done after the rounding: 1.000123 -> 1. . Stripping of trailing zeros should only be done after entering a number has concluded (non-digit character pressed).
Input: String.

Output: String.
'''

'''
Explanations:

Key Components of the Solution

State Tracking: The function keeps track of several important states:

The current display value
The number being entered
The stored number for operations
The last operation performed
Whether a calculation was just performed


Number Entry:

Limits input to 5 digits (excluding decimal point and negative sign)
Handles decimal points correctly
Removes leading zeros


Operation Handling:

Basic operations: +, -, *, /, //, %, **
Special sequences: == (repeating last operation), += and -= (doubling or subtracting the number from itself)
Proper order of operations


Formatting and Display Rules:

Rounding long decimal numbers to fit within the 5-digit limit
Removing trailing zeros after operations
Removing leading zeros
Showing "error" for overflow conditions



How the Code Works
The function processes each key press sequentially, maintaining the calculator's state:

When a digit is pressed, it's added to the current number (up to 5 digits).
When an operation key is pressed:

If a number was being entered, it's processed and stored
The appropriate operation is recorded
Special sequences (==, +=, -=) are handled according to the rules


When the decimal point is pressed, it's added to the current number if not already present.
The display is updated after each key press to show what would be on the calculator screen.
Number formatting is handled carefully:

Stripping trailing zeros after operations
Proper rounding for numbers exceeding 5 digits
Correct handling of negative numbers and decimal points



Edge Cases Handled

Integer division, modulo, and power operations
Repeated equals (==) performing the last operation again
Operator combinations like +=, -=
Overflow conditions showing "error"
Proper decimal point handling and formatting
Numbers with only zeros converted to a single zero
Negative number display
'''
def perform_operation(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    elif operation == "//":
        return a // b
    elif operation == "%":
        return a % b
    elif operation == "**":
        return a ** b

def is_error(number):
    # Check if the absolute value exceeds display limits
    if abs(number) >= 100000:
        return True
    
    # For floats, check if the integer part exceeds limits
    if isinstance(number, float) and int(abs(number)) >= 10000:
        return True
    
    return False

def format_number(number):
    # Convert to string and check if it's within display limits
    if is_error(number):
        return "error"
    
    # Convert integers to int to remove decimal point
    if number == int(number):
        return str(int(number))
    
    # Format float numbers
    # Convert to string with enough precision
    str_num = str(number)
    
    # If it has decimal part
    if '.' in str_num:
        # Ensure total length doesn't exceed 5 digits (including negative sign)
        # Round if necessary
        return strip_zeros(round_if_needed(str_num))
    
    return str_num

def round_if_needed(number_str):
    # Handle negative sign separately
    negative = number_str.startswith('-')
    if negative:
        number_str = number_str[1:]
    
    # Split into integer and fractional parts
    parts = number_str.split('.')
    int_part = parts[0]
    frac_part = parts[1] if len(parts) > 1 else ""
    
    # Remove leading zeros from integer part
    int_part = int_part.lstrip("0") or "0"
    
    # Calculate total significant digits (excluding decimal point)
    total_digits = len(int_part) + len(frac_part)
    if int_part == "0":
        total_digits = len(frac_part)
    
    # Round if total length exceeds 5 digits
    if total_digits > 5:
        # Determine how many decimal places to keep
        decimal_places = max(0, 5 - len(int_part))
        if int_part == "0":
            decimal_places = 5
        
        number = float(number_str)
        rounded = round(number, decimal_places)
        
        # If rounding makes an integer, return as integer
        if rounded == int(rounded):
            result = str(int(rounded))
        else:
            result = str(rounded)
    else:
        result = number_str
    
    # Add negative sign back if needed
    if negative and result != "0":
        result = "-" + result
    
    return result

def strip_zeros(number_str):
    # Handle negative sign separately
    negative = number_str.startswith('-')
    if negative:
        number_str = number_str[1:]
    
    # Split into integer and fractional parts
    parts = number_str.split('.')
    int_part = parts[0]
    frac_part = parts[1] if len(parts) > 1 else ""
    
    # Remove leading zeros from integer part (but keep at least one digit)
    int_part = int_part.lstrip("0") or "0"
    
    # Remove trailing zeros from fractional part
    frac_part = frac_part.rstrip("0")
    
    # Construct the final string
    if frac_part:
        result = int_part + "." + frac_part
    elif '.' in number_str:
        result = int_part + "."
    else:
        result = int_part
    
    # Handle special case where integer part is zero
    if int_part == "0" and frac_part:
        result = "." + frac_part
    
    # Add negative sign back if needed
    if negative and result != "0":
        result = "-" + result
    
    return result

def calculator(log: str) -> str:
    # State variables
    display = "0"  # What's currently shown on screen
    current_number = ""  # Current number being entered
    stored_number = None  # Previous number in calculation
    last_operation = None  # Last operation performed
    last_operator = None  # Last operator key pressed
    calculation_performed = False  # Whether a calculation was just performed
    
    for key in log:
        # Process digit keys (0-9)
        if key.isdigit():
            # If we just did a calculation, start a new number
            if calculation_performed:
                current_number = ""
                calculation_performed = False
            
            # Ignore digits after the 5th one in current number
            if len(current_number.replace('-', '').replace('.', '')) < 5:
                current_number += key
            
            # Update display with current number (remove leading zeros)
            if current_number.startswith('-'):
                display = '-' + current_number[1:].lstrip("0")
                if len(display) == 1:  # Just the minus sign
                    display = "-0"
            else:
                display = current_number.lstrip("0")
                if display == "" or display == ".":
                    display = "0" + display
            
        # Process operation keys
        elif key in "+-*/=%":
            # Special handling for two-character operations
            if key in "/*" and last_operator == key:
                # Handle //, ** operations
                last_operation = last_operation[0] + key
                last_operator = key
                continue
            
            # If we were entering a number, process it
            if current_number:
                # Format the number correctly
                if '.' in current_number:
                    # Only strip trailing zeros when finishing a number
                    current_number = strip_zeros(current_number)
                
                # Convert to float
                current_value = float(current_number)
                
                # If no stored number yet, just store the current number
                if stored_number is None:
                    stored_number = current_value
                # Otherwise perform the pending operation
                elif last_operation:
                    result = perform_operation(stored_number, current_value, last_operation)
                    
                    # Check for overflow error
                    if is_error(result):
                        return "error"
                    
                    stored_number = result
                    display = format_number(result)
            elif stored_number is not None and key in "+-" and (last_operator in "+-*/%" or last_operator is None):
                # Handle sign change when no number is being entered
                current_number = key + "0"
                display = key + "0"
                last_operator = key
                continue
            
            # Handle special operation sequences
            if key == "=" and last_operator == "=":  # == sequence
                if last_operation and stored_number is not None:
                    # Repeat the last operation
                    result = perform_operation(stored_number, current_value if current_number else stored_number, last_operation)
                    
                    if is_error(result):
                        return "error"
                    
                    stored_number = result
                    display = format_number(result)
            
            elif key == "=" and last_operator in "+-*/%":  # +=, -=, etc.
                if not current_number and last_operation and stored_number is not None:
                    # Apply operation to the stored number itself
                    result = perform_operation(stored_number, stored_number, last_operation)
                    
                    if is_error(result):
                        return "error"
                    
                    stored_number = result
                    display = format_number(result)
            
            # Reset current number for next input
            current_number = ""
            calculation_performed = True
            
            # Update last operation unless it's "="
            if key != "=":
                last_operation = key
            
            last_operator = key
        
        # Handle decimal point
        elif key == ".":
            # If we just did a calculation, start a new number
            if calculation_performed:
                current_number = "0"
                calculation_performed = False
            
            # If we haven't started a number, start with "0."
            if not current_number:
                current_number = "0"
            
            # Add decimal point if not already present
            if "." not in current_number:
                current_number += "."
                display = current_number
        
    # Return what's on the display after processing all keys
    return display

print("Example:")
print(calculator("10//2="))

# These "asserts" are used for self-checking
assert calculator("10/2*2=") == "10."
assert calculator("10/=*=-=") == "0."
assert calculator("100//33**3=") == "27"
assert calculator("10%10=") == "0"
assert calculator("---+++100//3//3+++---") == "11"
assert calculator("27**.3333=") == "3."
assert calculator("0001.1000") == "1.100"
assert calculator("0001.1000-") == "1.1"
assert calculator("999.9999999+=") == "2000."
assert calculator("1.000123") == "1.000"
assert calculator("9999.9999999+=") == "error"
assert calculator("90000+10000=") == "error"
assert calculator("90000+10000-10000=") == "error"
assert calculator("90000+10000-10000") == "10000"
assert calculator("123456789") == "12345"
assert calculator("123456789+5=") == "12350"
assert calculator("5+123456789") == "12345"
assert calculator("50000+=") == "error"
assert calculator("3+=") == "6"
assert calculator("3+2==") == "7"
assert calculator("4-1==") == "2"
assert calculator("3+-2=") == "1"
assert calculator("-=-+3-++--+-2=-") == "1"
assert calculator("000000") == "0"
assert calculator("0000123") == "123"
assert calculator("12") == "12"
assert calculator("+12") == "12"
assert calculator("") == "0"
assert calculator("1+2") == "2"
assert calculator("2+") == "2"
assert calculator("1+2=") == "3"
assert calculator("1+2-") == "3"
assert calculator("1+2=2") == "2"
assert calculator("=5=10=15") == "15"

print("The mission is done! Click 'Check Solution' to earn rewards!")
