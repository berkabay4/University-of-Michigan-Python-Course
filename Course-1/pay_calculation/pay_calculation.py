# Write a program to prompt the user for hours and rate per hour
# using input to compute gross pay. Pay the hourly rate for the hours
# up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.

# Use 45 hours and a rate of 10.50 per hour to test the program
# (the pay should be 498.75).
# You should use input to read a string and float()
# to convert the string to a number.

# Do not worry about error checking the user
# input - assume the user types numbers properly.


# Take input values from user
shrs = input("Enter Hours:")
srate = input("Enter Rate:")

# Is this inputs are numeric input ?
try:
    fhrs = float(shrs)
    frate = float(srate)

except:
    print("Error, please enter numeric input.")

# If working hour bigger than 40,
if fhrs > 40:
    ahrs = fhrs - 40
    pay = (40.0 * frate) + (ahrs * frate * 1.5)

# If working hour equal or smaller than 40,
else:
    pay = fhrs*frate

# Print value
print("Pay:", pay)
