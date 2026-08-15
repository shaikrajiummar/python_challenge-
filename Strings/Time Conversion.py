time_str = input()

if time_str.endswith("M"):
  minutes = int(time_str[:-1])
  hours = round(minutes / 60, 2)
  print(f"{hours}H")
elif time_str.endswith("S"):
  seconds = int(time_str[:-1])
  hours = round(seconds / 3600, 2)
  print(f"{hours}H")