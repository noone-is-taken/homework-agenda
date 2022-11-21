import calendar
import datetime
import os
from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button

#Const

FILENAME = "database.txt"
date = datetime.datetime.now()

#class and functions

class Homework:
    def __init__(self,homeworkToDo,daydue):
        self.homeworkToDo = homeworkToDo
        self.daydue = daydue

    def text(self):
        return str(self.homeworkToDo)+" "+str(self.daydue)
    def dateNumber(self):
        try:
            day = self.daydue.split("/")
            return int(day[0])+int(day[1])*100
        except:
            return 0
    def get_all(self):
        return str(self.homeworkToDo)+","+str(self.daydue)+"\n"


def renewHomeWork():
    global homeworkText
    homeworkText = "Todays homework is: \n"
    i = 0
    if homeWorkArray:
        orderHomeworkArray()
        for hw in homeWorkArray:
            tmp =  homeworkText + hw.text() + " "+str(i) + "\n"
            homeworkText = tmp 
            i += 1


def entraHomeWorks():
    global homeworkText
    homeWorkArray.append(Homework(homeworkToDo.get(),daydue.get()))
    
    with open(FILENAME,'a+') as f:
        f.write(homeworkToDo.get())
        f.write(',')
        f.write(daydue.get())
        f.write('\n')
    renewHomeWork()
    tdayHomewokr.configure(text=homeworkText)

    #clear the entrys
    homeworkToDo.delete(0,'end')
    daydue.delete(0,'end')

def eliminateHomeworks():
    global homeworkText
    #gets the index of the line that we want to remove
    indexToEliminate = int(eliminateEntry.get())
    #delets the line in local array and renew visual homework
    del homeWorkArray[indexToEliminate]
    
    renewHomeWork()
    tdayHomewokr.configure(text=homeworkText)
    #delet the line in the file so next time we open is not there
    #open the file and get all the lines
    databaseFile = open(FILENAME,"r")
    lines = databaseFile.readlines()
    databaseFile.close
    #we delet the line
    lines = homeWorkArray
    #create the same file but empty
    newDataBase = open(FILENAME,"w+")
    #replace with all the lines without the one that we delted
    for line in lines:
        newDataBase.write(line.get_all())

    newDataBase.close()

    #clear delet entry
    eliminateEntry.delete(0,'end')

def intToMonth(number):
    if(number==1):
        return "January"
    elif(number==2):
        return "February"
    elif(number==3):
        return "March"
    elif(number==4):
        return "April"
    elif(number==5):
        return "May"
    elif(number==6):
        return "June"
    elif(number==7):
        return "July"
    elif(number==8):
        return "August"
    elif(number==9):
        return "September"
    elif(number==10):
        return "October"
    elif(number==11):
        return "November"
    elif(number==12):
        return "December"

def orderHomeworkArray():
    f = open(FILENAME,"r+")
    f.truncate(0)
    f.close()
    for j in range(len(homeWorkArray)):
        for i in range(len(homeWorkArray)):
            noError = j
            if(noError==546468516):
                print("noerror")
            if(i<len(homeWorkArray)-1):
                if(homeWorkArray[i].dateNumber()>homeWorkArray[i+1].dateNumber()):
                    t = homeWorkArray[i]
                    homeWorkArray[i] = homeWorkArray[i+1]
                    homeWorkArray[i+1] = t
    
    lines = homeWorkArray
    #create the same file but empty
    newDataBase = open(FILENAME,"w+")
    #replace with all the lines without the one that we delted
    for line in lines:
        newDataBase.write(line.get_all())

    newDataBase.close()
    


    



homeWorkArray = []

#end class

#opening bdd


    
try:#try to open the data base and chek what is inside
    with open(FILENAME,'r') as f:
        if(os.path.getsize(FILENAME)!=0):
            for line in f:
                line = line.rstrip('\n')
                hw = line.split(',')
                homeWorkArray.append(Homework(str(hw[0]),str(hw[1])))
except IOError:#if the file does not exist then we create the file
    f = open(FILENAME,'w+')
    f.close()

orderHomeworkArray()








c = calendar.month(date.year,date.month)
#visual things
root = Tk()
root.geometry("620x300")
root.title("Agenda")

app = Frame(root)
app.grid()

month = Label(app, text=c, font=('Consolas', 12))
month.grid(row=0, column=0)

cNext = calendar.month(date.year,date.month+1)

nextMonth = Label(app, text=cNext, font=('Consolas', 12))
nextMonth.grid(row=0,column=1,padx=15)


tdaytext =  "Today is \n" + str(date.day)+" of "+ intToMonth(date.month)

tdayt = Label(app, text=tdaytext, font=('Consolas', 12))
tdayt.grid(row=0,column=2)

homeworkText = "Todays homework is: \n"

#buttons and functions

renewHomeWork()

entryContainer = Frame(app)
entryContainer.grid(column=1,row=1,padx=10)

homeworkToDo = Entry(entryContainer,width=10)

homeworkToDo.grid(column=0, row=0,padx=5)

daydue = Entry(entryContainer,width=5)

daydue.grid(column=1, row=0,padx=5)

doneButton = Button(entryContainer, text="Done",command=entraHomeWorks)

doneButton.grid(column=1,row=1,padx=5)


elemiContainer = Frame(app)
elemiContainer.grid(column=2,row=1,padx=10)
eliminateEntry = Entry(elemiContainer,width=10)

eliminateEntry.grid(column=0,row=0)

elimButton = Button(elemiContainer, text="Eliminate",command=eliminateHomeworks)
elimButton.grid(column=0,row=1)

tdayHomewokr = Label(app, text=homeworkText,font=('Consolas', 12))
tdayHomewokr.grid(row=1,column=0)

root.mainloop()
