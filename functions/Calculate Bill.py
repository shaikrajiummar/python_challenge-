def calculate_bill(amount):
    # Complete this function
    if amount < 500:
        discount = 0.05 * amount
    elif 500 <= amount < 2500:
        discount = 0.10 * amount
    else:
        discount = 0.20 * amount

    return amount - discount


amount = int(input())
# Call the calculate_bill function
result = calculate_bill(amount)
print(result)