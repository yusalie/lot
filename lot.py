# Imports libraries
from tkinter import *
from tkinter import messagebox as mb
from random import sample as rnd
from tkinter import ttk
from datetime import *

# Empty list for the inputs
li = []
# Random number generator
random_num = rnd(range(1,49),6)

# First instance of tkinter
app = Tk()
app.geometry("220x120")
app.resizable(False,False)

# wigdets
# Handles the entry and labels of the first window
id_num = Entry(app)
id_lb = Label(app,text="ID no.:")

age_lb = Label(app,text="Age:")
age_ = Entry(app,text="age:",width=5)

name_ = Entry(app)
name_lb = Label(app, text="Name:")

dt_lb = Label(app)
dt_lb.config(text="Date: "+datetime.now().strftime("%m/%d/%y"))

# Creates the txt file
file = "Lotto.txt"

# function to check age and open the results for the lotto
def chck_age():
    try:
        # Descion tree to descide how old you
        #and if youre alowed in
        if int(age_.get()) < 18:
            mb.showwarning("Underage", "You are not old enough")
        if int(age_.get()) < 0:
            mb.showerror("Error", "Enter a number greater than 0")
        if int(age_.get()) >= 18:
            # creates variables to store name, ID and age
            nameVar = name_.get()
            ageVar = age_.get()
            idVar = id_num.get()
            dtVar = str(dt_lb.cget("text"))
            app.destroy()
            # Creates second instance of tkinter
            window = Tk()
            window.title("Lottery Result")
            window.geometry("350x550")
            window.resizable(False,False)

        try:
            # Creates widgets to enter numbers
            # and labels
            num1 = Entry(window,width=5)
            num2 = Entry(window,width=5)
            num3 = Entry(window,width=5)
            num4 = Entry(window,width=5)
            num5 = Entry(window,width=5)
            num6 = Entry(window,width=5)
            lb = Label(window, text="Enter Lotto numbers:")
            result_lb = Label(window)
        except ValueError as e:
            mb.showerror("Error", "Enter number"+e)
            # function to append the list and 
            # decide how many numbers you got correct
        def lot_():
            str_var = StringVar()
            li.append(int(num1.get()))
            li.append(int(num2.get()))
            li.append(int(num3.get()))
            li.append(int(num4.get()))
            li.append(int(num5.get()))
            li.append(int(num6.get()))
            
            # Checks how many numbers you got correct
            num_correct = set(li).intersection(random_num)
            # Desicion tree
            if li == random_num:
                result_lb.config(text="Name: "+nameVar+"\n"+"ID: "+idVar+"\n"+"Age: "+ageVar+"\n"+"You got all correct\n" + "The results were: " + str(sorted(random_num[0:5])) +"\n" +"Jackpot ball is: "+ str(random_num[5]) +"\n"+"YOU WON R10 000 000.00"+"\n"+dtVar)
            elif len(num_correct) == 0:    
                result_lb.config(text="Name: "+nameVar+"\n"+"ID: "+idVar+"\n"+"Age: "+ageVar+"Sorry you got 0 correct\n" + "The results were: " + str(sorted(random_num[0:5])) +"\n" +"Jackpot ball is: "+ str(random_num[5]) +"\n"+"You won nothing..."+"\n"+dtVar)
            elif len(num_correct) == 1:    
                result_lb.config(text="Name: "+nameVar+"\n"+"ID: "+idVar+"\n"+"Age: "+ageVar+"Sorry you got 1 correct\n" + "The results were: " + str(sorted(random_num[0:5])) +"\n" +"Jackpot ball is: "+ str(random_num[5]) +"\n"+"You won nothing..."+"\n"+dtVar)
            elif len(num_correct) == 2:    
                result_lb.config(text="Name: "+nameVar+"\n"+"ID: "+idVar+"\n"+"Age: "+ageVar+"Sorry you got 2 correct\n" + "The results were: " + str(sorted(random_num[0:5])) +"\n" +"Jackpot ball is: "+ str(random_num[5]) +"\n"+"You won R20"+"\n"+"\n"+dtVar)
            elif len(num_correct) == 3:    
                result_lb.config(text="Name: "+nameVar+"\n"+"ID: "+idVar+"\n"+"Age: "+ageVar+"Sorry you got 3 correct\n" + "The results were: " + str(sorted(random_num[0:5])) +"\n" +"Jackpot ball is: "+ str(random_num[5]) +"\n"+"You won R100.50"+"\n"+"\n"+dtVar)
            elif len(num_correct) == 4:    
                result_lb.config(text="Name: "+nameVar+"\n"+"ID: "+idVar+"\n"+"Age: "+ageVar+"Sorry you got 4 correct\n" + "The results were: " + str(sorted(random_num[0:5])) +"\n" +"Jackpot ball is: "+ str(random_num[5]) +"\n"+"You won R2,384.00"+"\n"+dtVar)
            elif len(num_correct) == 5:    
                result_lb.config(text="Name: "+nameVar+"\n"+"ID: "+idVar+"\n"+"Age: "+ageVar+"Sorry you got 5 correct\n" + "The results were: " + str(sorted(random_num[0:5])) +"\n" +"Jackpot ball is: "+ str(random_num[5]) +"\n"+"You won R8,584.00"+"\n"+dtVar)
            f = open(file, "w+")
            f.close()
            f = open(file, "a")
            results = result_lb.cget("text")
            f.write(results)
            f.close()
        # Button to use function lot_
        lot_btn = Button(window, text="Check Results", command=lot_)
        
        # Places widgets
        lb.place(x=1,y=1)
        num1.place(x=1,y=25)
        num2.place(x=45,y=25)
        num3.place(x=90,y=25)
        num4.place(x=135,y=25)
        num5.place(x=180,y=25)
        num6.place(x=225,y=25)
        lot_btn.place(x=1,y=49)
        result_lb.place(x=1,y=98)
        window.mainloop()
    except:
        mb.showinfo("", "enter number")

# Button that uses function
entr_btn = Button(app, command=chck_age, text="Enter Lotto")

#places Widgets from first instance
name_lb.place(x=1,y=1)
name_.place(x=50, y=1)
id_lb.place(x=1,y=30)
id_num.place(x=50,y=30)
age_lb.place(x=1,y=60)
age_.place(x=50, y=60)
entr_btn.place(x=1,y=90)
dt_lb.place(x=110,y=100)
app.mainloop()