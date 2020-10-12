import tkinter
import random

class MyGUI:
    def __init__(self,num):
        self.main_window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.main_window,width = 400, height = 400)
        self.canvas.create_rectangle(20,20,360,360) 
        

        if num ==1:
            self.canvas.create_oval(160,160,220,220,fill="black") #中心点
        elif num ==2:
            self.canvas.create_oval(40,40,100,100,fill="black") #左上
            self.canvas.create_oval(340,340,280,280,fill="black") #右下
        elif num == 3:
            self.canvas.create_oval(40,40,100,100,fill="black") #左上
            self.canvas.create_oval(160,160,220,220,fill="black") #中心点
            self.canvas.create_oval(340,340,280,280,fill="black") #右下
        elif num==4:
            self.canvas.create_oval(40,40,100,100,fill="black") #左上
            self.canvas.create_oval(340,340,280,280,fill="black") #右下
            self.canvas.create_oval(40,340,100,280,fill="black") #左下
            self.canvas.create_oval(340,40,280,100,fill="black") #右上
        elif num == 5:
            self.canvas.create_oval(40,40,100,100,fill="black") #左上
            self.canvas.create_oval(340,340,280,280,fill="black") #右下
            self.canvas.create_oval(40,340,100,280,fill="black") #左下
            self.canvas.create_oval(340,40,280,100,fill="black") #右上
            self.canvas.create_oval(160,160,220,220,fill="black") #中心点
        else :
            self.canvas.create_oval(40,40,100,100,fill="black") #左上
            self.canvas.create_oval(340,340,280,280,fill="black") #右下
            self.canvas.create_oval(40,340,100,280,fill="black") #左下
            self.canvas.create_oval(340,40,280,100,fill="black") #右上
            self.canvas.create_oval(40,160,100,220,fill="black") #中左
            self.canvas.create_oval(280,160,340,220,fill="black") #中右

        self.canvas.pack()
        tkinter.mainloop()

num=random.randint(1,6)
gui=MyGUI(num)

