from tkinter import *
import math

def leftCLick(event):
    print(float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2))
    BMI = float(textboxWeight.get())/math.pow(float(textboxHeight.get())/100,2)
    if BMI > 30:
        labelResult.configure(text="อ้วนมาก")
    elif BMI >= 25:
        labelResult.configure(text="อ้วนระดับ2")
    elif BMI >= 23:
        labelResult.configure(text="อ้วนระดับ1")
    elif BMI >= 18.5:
        labelResult.configure(text="ปกติ")
    elif BMI < 18.5:
        labelResult.configure(text="ผอม")

mainWindow = Tk()
labelHeight = Label(mainWindow,text="ส่วนสูง (CM)")
textboxHeight = Entry(mainWindow)
labelWeight = Label(mainWindow,text="น้ำหนัก (KG)")
textboxWeight = Entry(mainWindow)
labelHeight.grid(row=0,column=0)
textboxHeight.grid(row=0,column=1)
labelWeight.grid(row=1,column=0)
textboxWeight.grid(row=1,column=1)
CalculatorBMI = Button(mainWindow,text="คำนวณ")
CalculatorBMI.grid(row=2)
CalculatorBMI.bind("<Button-1>",leftCLick)
labelResult = Label(mainWindow,text="BMI = ")
labelResult.grid(row=2,column=1)
mainWindow.mainloop()




