# Week 1.2, Session 2: Task 6

temperature = int(input("Input the temperature of the machine(\u00b0C): "))
pressure = int(input("Input the pressure of the machine(PSI): "))
status = input("Is the machine on?(y/n): ")
if status.lower() == "y":
    status = True
elif status.lower() == "n":
    status = False
else:
    print("Invalid status.")

if status:
    if temperature > 80:
        print("Temperature too high, shutdown recommended.")
    elif temperature > 50:
        print("Temperature in safe limits.")
    else:
        print("Temperature is low.")
    if pressure > 100:
        print("High pressure, maintenance recommended.")
    elif pressure > 30:
        print("Pressure is stable.")
    else:
        print("Pressure is low.")
else:
    print("Machine is not running.")
