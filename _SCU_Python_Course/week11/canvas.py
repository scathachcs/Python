import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.canvas = tkinter.Canvas(self.main_window,width = 400, height = 400)

        self.canvas.create_text(200,200,text = "This is the final work of Python class")

        self.canvas.create_line(10,10,390,10)

        self.canvas.create_oval(20,20,360,360)

        self.canvas.create_rectangle(20,20,360,360)

        self.canvas.pack()

        tkinter.mainloop()

my_gui = MyGUI()