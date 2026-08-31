def validate_atm_pin_code(pin):
    # Complete this function
    is_valid_length = len(pin) == 4 or len(pin) == 6
    is_all_digits = pin.isdigit()

    if is_valid_length and is_all_digits:
        return "Valid PIN Code"
    else:
        return "Invalid PIN Code"


pin = input()
# Call the validate_atm_pin_code function
result = validate_atm_pin_code(pin)
print(result)