#calculations

def calculate():
    totalSal = 0
    x_place = 150
    bi_weeklyy = []
    for h in create_Hour_input():
        for w in create_Wage_input():
            print(h)
            hour_tot = float(h.get())
            wage_tot = float(w.get())
            bi_weekly = ((hour_tot * wage_tot * 2) * 100) / 100
            totalSal += bi_weekly
            bi_weeklyy.append(bi_weekly)

    for i in bi_weeklyy:
        bi_weekly_tot = Label(root, text= i, bg='paleturquoise').place(x= x_place, y=150)
        totalSal = Label(root, text= totalSal, bg='paleturquoise').place(x=210, y=180)
        x_place += 60
        return bi_weekly_tot, totalSal


def clear():
    for h in create_Hour_input():
        for w in create_Wage_input():
            h.delete(0,END)
            w.delete(0,END)

    tot = Label(root,width=23, fg='paleturquoise', bg='paleturquoise')
    tot.place(x=140, y=150)
    tot_sal = Label(root,width=15, fg='paleturquoise', bg='paleturquoise')
    tot_sal.place(x=170, y=180)
    return tot, tot_sal

def create_Wage_input():
    wage_inputt = []
    x_place = 130
    for i in range(3):
        wage = Entry(root, width=10)
        wage.place(x=x_place,y=110)
        x_place += 60
        wage_inputt.append(wage)
    return wage_inputt

def create_Hour_input():
    hour_inputt = []
    x_place = 130
    for i in range(3):
        hour = Entry(root, width=10)
        hour.place(x=x_place,y=70)
        x_place += 60
        hour_inputt.append(hour)
    return hour_inputt

def create_Job_label():
    x_place = 140
    jobs = ["1st Job", "2nd Job", "3rd Job"]
    final = []
    for i in range(3):
        job_label = Label(root, text= jobs[i], bg='paleturquoise')
        job_label.place(x = x_place, y = 40)
        x_place += 60
        final.append(job_label)
    return final

#import module
from tkinter import *
#create object
root = Tk()

#set size
root.geometry('450x300')

# Create background
root.configure(background ='paleturquoise')

#create labels
salary_label = Label(root,text= 'Pre-Tax Weekly Salary Calculator', bg='orchid',justify=CENTER).pack()

create_Job_label()

hours_worked = Label(root, text = "Hours Worked").place(x = 40,y = 70)
create_Hour_input()

wage = Label(root, text = "Wage per hour").place(x = 40,y = 110)
create_Wage_input()

bi_weekly_wage = Label(root, text="Bi-weekly Salary").place(x = 40, y = 150)
total = Label(root, text="Sum of Salaries").place(x = 40, y = 180)

for i in range(3):
    calc_button = Button(root, text= "Calculate", bg='orchid', justify=CENTER, command = calculate).place(x =170,y=220)

clear = Button(root, text= "Clear", bg='orchid', justify=CENTER, command = clear).place(x =230,y=220)

label = Label(root, text = "Insert Zeros if less than 3 jobs").place(x = 140,y = 250)

root.mainloop()





