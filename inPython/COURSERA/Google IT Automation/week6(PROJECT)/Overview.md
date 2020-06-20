# PROJECT OVERVIEW

## PROBLEM STATEMENT

We need to process a list of event objects using their date, type, machine, and user attributes to generate a report that lists all users currently logged into the machines.

## RESEARCH

To find out which users are currently logged in and when they logged out. If a user logged into a machine and then logged out, they're no longer logged into it. But if they didn't logout yet, they're still logged in.

## PLANNING

When we process an event, we'll see that someone interacted with a machine. If it's a login, we wamt to add it to the group of users logged into the machine.
If it's a logout, we want to remove it from the grooup of users logged into the machine. We would use a set to store the current users, adding new users at login time and removing them at logout time.
But then, the best way would be to store our information in a **DICTIONARY**. We'll use the name of the machine as the key and the current users of that machine as the value. SO for each event we process, we'll first check in the dictionary to see if the machine is already there.


