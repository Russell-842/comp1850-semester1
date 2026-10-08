# Week 1.2, Session 2: Task 6
# Task 6

# Step 1 : Get User inputs
# You need to collect three inputs from the user:

# 1. The machine's temperature in degrees Celsius (integer)
temperature = int(input("Enter the machine's temperature in degrees Celsius : "))
print(temperature)
# 2. The machine's pressure in PSI (integer)
pressure = int(input("Enter the machine's pressure in PSI : "))
print(pressure)
# 3. The machine's operational status (1 for operating, 0 for stopped) (integer)
operationalstatus = int(input("Enter the machine's operational status : "))
if operationalstatus == 1 : 
    print("Operating")
else :
    print("Stopped")

# Step 2 : Evaluate Operating Conditions
# Use conditional statements involving `if`, `elif` and `else` to evaluate the operating temperature and pressure of the machine.
# Temperature
if temperature > 80 :
   print("The temperature is too high. Shutting down the machine is recommended.")
elif temperature >= 50 and 80 :
   print("The temperature is within safe limits. The temperature is within safe limits.")
else :
   print("The machine temperature is low and no action is needed.")

# Pressure
if pressure > 100 :
   print("High pressure is detected. Maintenance is recommended.")
elif pressure >= 70 and 100 :
   print("The pressure is stable.")
else : 
   print("The pressure is low and the system is operating normally.")

# Step 3 : Determine Status
