# Here is a Program that turns a number of seconds into more human readable
# count of hours, minutes and seconds.
# a call to input() allows user to enter the number of seconds.
# then we convert that string to an integer.

str_seconds = input("Please enter the number of seconds you wish to convert") #Remember an input is originally in strings
total_secs = int(str_seconds) ##Converting the stringed input to int

hours = total_secs // 3600 
secs_still_remaining = total_secs % 3600
minutes = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60

print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining)
