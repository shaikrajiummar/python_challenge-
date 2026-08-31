def get_speed_status(speed):
    # Complete this function
    if speed < 60:
        return "Normal"
    elif 60 <= speed < 80:
        return "Warning"
    else:
        return "Over Speed"


speed = int(input())
# Call the get_speed_status function
result = get_speed_status(speed)
print(result)