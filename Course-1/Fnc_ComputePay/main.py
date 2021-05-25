# Write a program to prompt the user for hours and rate per hour using
# input to compute gross pay. Pay should be the normal rate for hours
# up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours.

# Put the logic to do the computation of pay in a function called computepay()
# and use the function to do the computation. The function should return a value.

# Define computepay function
def computepay(h, r):
# If working hour bigger than 40,
    if h > 40:
        ahrs = h - 40
        pay = (40.0 * r) + (ahrs * r * 1.5)
# If working hour equal or smaller than 40,
    else:
        pay = h * r
# Return calculated value
    return pay

# Take input values from user
hrs  = input("Enter Hours:")
rate = input("Enter Rate:")

# Is this inputs are numeric input ?
try:
    fhrs = float(hrs)
    frate = float(rate)

except:
    print("Error, please enter numeric input.")

# Invoke computepay function
p = computepay(fhrs, frate)

# Print value
print("Pay", p)