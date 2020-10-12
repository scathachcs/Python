import tkinter;

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.frame = tkinter.Frame()
        self.line_button = tkinter.Button(self.frame,text='绘制直线',command=self.line)#按键1
        self.rect_button = tkinter.Button(self.frame,text='绘制矩形',command=self.rect)#按键2
        self.circ_button = tkinter.Button(self.frame, text='绘制圆形',command=self.circ)#按键3
        self.line_button.pack(side = 'left')
        self.rect_button.pack(side = 'left')
        self.circ_button.pack(side = 'left')

        self.frame.pack()
        self.main_window.mainloop()

    def line(self):
        self.line_window = tkinter.Tk()
        self.line_frame = tkinter.Frame(self.line_window)

        self.Var1_label = tkinter.Label(self.line_frame,text = 'X1: ')
        self.Var1_Entry = tkinter.Entry(self.line_frame,width = 40)

        self.Var2_label = tkinter.Label(self.line_frame,text = 'Y1: ')
        self.Var2_Entry = tkinter.Entry(self.line_frame,width = 40)

        self.Var3_label = tkinter.Label(self.line_frame,text = 'X2: ')
        self.Var3_Entry = tkinter.Entry(self.line_frame,width = 40)

        self.Var4_label = tkinter.Label(self.line_frame,text = 'Y2: ')
        self.Var4_Entry = tkinter.Entry(self.line_frame,width = 40)

        self.line_check_button = tkinter.Button(self.line_frame,text='确认',command=self.draw_line)#确认按键

        self.Var1_label.pack(side='left')
        self.Var1_Entry.pack(side='left')

        self.Var2_label.pack(side='left')
        self.Var2_Entry.pack(side='left')

        self.Var3_label.pack(side='left')
        self.Var3_Entry.pack(side='left')

        self.Var4_label.pack(side='left')
        self.Var4_Entry.pack(side='left')
        self.line_check_button.pack(side='left')
        self.line_frame.pack()
        self.line_canvas = tkinter.Canvas(self.line_window,width = 400, height = 400)
        self.line_canvas.pack()
        self.line_window.mainloop()

    def rect(self):
        self.rect_window = tkinter.Tk()
        self.rect_frame = tkinter.Frame(self.rect_window)

        self.Var5_label = tkinter.Label(self.rect_frame,text = 'X1: ')
        self.Var5_Entry = tkinter.Entry(self.rect_frame,width = 40)

        self.Var6_label = tkinter.Label(self.rect_frame,text = 'Y1: ')
        self.Var6_Entry = tkinter.Entry(self.rect_frame,width = 40)

        self.Var7_label = tkinter.Label(self.rect_frame,text = 'X2: ')
        self.Var7_Entry = tkinter.Entry(self.rect_frame,width = 40)

        self.Var8_label = tkinter.Label(self.rect_frame,text = 'Y2: ')
        self.Var8_Entry = tkinter.Entry(self.rect_frame,width = 40)

        self.rect_check_button = tkinter.Button(self.rect_frame,text='确认',command=self.draw_rect)#确认按键

        self.Var5_label.pack(side='left')
        self.Var5_Entry.pack(side='left')

        self.Var6_label.pack(side='left')
        self.Var6_Entry.pack(side='left')

        self.Var7_label.pack(side='left')
        self.Var7_Entry.pack(side='left')

        self.Var8_label.pack(side='left')
        self.Var8_Entry.pack(side='left')
        self.rect_check_button.pack(side='left')
        self.rect_frame.pack()
        self.rect_canvas = tkinter.Canvas(self.rect_window,width = 400, height = 400)
        self.rect_canvas.pack()
        self.rect_window.mainloop()

    def circ(self):
        self.circ_window = tkinter.Tk()
        self.circ_frame = tkinter.Frame(self.circ_window)

        self.Var9_label = tkinter.Label(self.circ_frame,text = 'X: ')
        self.Var9_Entry = tkinter.Entry(self.circ_frame,width = 40)

        self.Var10_label = tkinter.Label(self.circ_frame,text = 'Y: ')
        self.Var10_Entry = tkinter.Entry(self.circ_frame,width = 40)

        self.Var11_label = tkinter.Label(self.circ_frame,text = 'R: ')
        self.Var11_Entry = tkinter.Entry(self.circ_frame,width = 40)


        self.circ_check_button = tkinter.Button(self.circ_frame,text='确认',command=self.draw_circ)#确认按键

        self.Var9_label.pack(side='left')
        self.Var9_Entry.pack(side='left')

        self.Var10_label.pack(side='left')
        self.Var10_Entry.pack(side='left')

        self.Var11_label.pack(side='left')
        self.Var11_Entry.pack(side='left')

        self.circ_check_button.pack(side='left')
        self.circ_frame.pack()
        self.circ_canvas = tkinter.Canvas(self.circ_window,width = 400, height = 400)
        self.circ_canvas.pack()
        self.circ_window.mainloop()

    def draw_line(self):
        x1=int(self.Var1_Entry.get())
        y1=int(self.Var2_Entry.get())
        x2=int(self.Var3_Entry.get())
        y2=int(self.Var4_Entry.get())
        self.line_canvas.create_line(x1,y1,x2,y2)

    def draw_rect(self):
        x1=int(self.Var5_Entry.get())
        y1=int(self.Var6_Entry.get())
        x2=int(self.Var7_Entry.get())
        y2=int(self.Var8_Entry.get())
        self.rect_canvas.create_rectangle(x1,y1,x2,y2)
    
    def draw_circ(self):
        x=int(self.Var9_Entry.get())
        y=int(self.Var10_Entry.get())
        r=int(self.Var11_Entry.get())
        self.circ_canvas.create_oval(x-r,y-r,x+r,y+r)

gui=MyGUI()   
