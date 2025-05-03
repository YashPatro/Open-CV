from tkinter import *
from tkinter import messagebox
import calendar
import time

def calculate_age():
    global dob
    dob = dob_entry.get() 
    dob_day, dob_month, dob_year = map(int, dob.split('/'))  
    today = time.localtime()  
    
    #year
    age_in_years = today.tm_year - dob_year - ((today.tm_mon, today.tm_mday) < (dob_month, dob_day))
    
    total_days = (today.tm_year - dob_year) * 365 + (today.tm_yday - dob_month) 

    total_seconds = total_days * 86400

    next_birthday_year = today.tm_year if today.tm_mon < dob_month or (today.tm_mon == dob_month and today.tm_mday < dob_day) else today.tm_year + 1
    next_birthday = time.localtime(time.mktime((next_birthday_year, dob_month, dob_day, 0, 0, 0, 0, 0, -1)))
    next_birthday_day_of_week = calendar.day_name[next_birthday.tm_wday] 
    
    global age_data
    age_data = {
        'years': age_in_years,
        'seconds': total_seconds,
        'days': total_days,
        'next_bday': next_birthday_day_of_week 
    }

    next_button.config(state=DISABLED)

def show_age_in_unit(unit):
    age = age_data.get(unit)
    if unit == 'next_bday':
        messagebox.showinfo(f"Your next birthday is:", f"Your next birthday will be on a {age}")
    else:
        messagebox.showinfo(f"Your age in {unit}:", f"Your age in {unit} is {age}")

#main window
root = Tk()
root.title("Age Calculator") 

label = Label(root, text="Enter your date of birth (DD/MM/YYYY):")
label.pack(pady=10) 

dob_entry = Entry(root)
dob_entry.pack(pady=20) 

next_button = Button(root, text="Next", command=calculate_age)
next_button.pack(pady=10)

years_button = Button(root, text="Years", command=lambda: show_age_in_unit('years'))
years_button.pack(pady=5)

seconds_button = Button(root, text="Seconds", command=lambda: show_age_in_unit('seconds'))
seconds_button.pack(pady=5)

days_button = Button(root, text="Days", command=lambda: show_age_in_unit('days'))
days_button.pack(pady=5)

next_bday_button = Button(root, text="Day of Next Birthday", command=lambda: show_age_in_unit('next_bday'))
next_bday_button.pack(pady=5)

root.mainloop()
