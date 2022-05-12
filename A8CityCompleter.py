"""
    City completer app written by David Johnson.
    Do not modify this file for assignment A8.
"""
from tkinter import Tk, Entry, Label
import A8

def get_city(city_string):
    global cities
    city = A8.binary_search_for_matching_string(city_string, cities)
    if city == None:
        label.config(text="No match")
    else:
        label.config(text=city)

def click(key):
    global city_string
    city_string =  city_string + key.char
    get_city(city_string)

def do_backspace(key):
    global city_string
    if city_string:
        city_string =  city_string[:-1]
    get_city(city_string)


city_string = ""

root = Tk()
root.title("City Completer")

entry = Entry(root, width=50)
#entry.grid()
# Bind entry to any keypress
entry.bind("<BackSpace>", do_backspace)
entry.bind("<Key>", click)
entry.pack()

cities = A8.lines_from_file("cities.txt")
cities.sort()

label = Label(root, width=50, anchor='w', fg="green")
label.pack()
root.mainloop()
