# UPPP-And-Out
This is the simple prototype of our bigger mobile app Up and Out.

Walkthrough of the code:
We would have list of events and places based on your location.
It will also have the list of times initialized

We initialized a python-dictionary that will act as a mvp of database.This dictionary would have its keys as user name and the list of their chosen events, places and times as a values.

Each user will be given the choices of events and will have to make one choice out of different choices.
After that user will be given the choices of places. User is allowed to choose only one place among the plethora of places available.
Finally, user is given the choice to choose the time range.

After the user is done choosing from all the categories, the program runs through the dictionary and finds out other person who chose the same event, same place and same time.
It will list out people with same interests, who want to go to same place, and who have same free time.

