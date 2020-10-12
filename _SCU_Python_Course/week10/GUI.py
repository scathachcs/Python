import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame()
        self.filecontent_frame = tkinter.Frame()
        self.fileaddress_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()


        self.BytesVar=tkinter.StringVar()#文件字符数显示
        self.BytesPrompt_label = tkinter.Label(self.top_frame,text = 'Num of Bytes: ')
        self.Bytes_label = tkinter.Label(self.top_frame,textvariable=self.BytesVar)
        self.BytesPrompt_label.pack(side='left')
        self.Bytes_label.pack(side='left')

        self.ContentPrompt_label = tkinter.Label(self.filecontent_frame,text='Content of File:')#文本框TEXT
        self.Content_text = tkinter.Text(self.filecontent_frame,width = 50,height= 10)
        self.ContentPrompt_label.pack(side='top')
        self.Content_text.pack(side='top')

        self.AddressVar = tkinter.StringVar()#地址输入Entry
        self.AddressPrompt_label = tkinter.Label(self.fileaddress_frame,text='Address of File: ')
        self.Address_Entry = tkinter.Entry(self.fileaddress_frame,width = 40,textvariable=self.AddressVar)
        self.AddressPrompt_label.pack(side='left')
        self.Address_Entry.pack(side='left')

        self.Read_button = tkinter.Button(self.bottom_frame,text='Read',command=self.read)#按键
        self.Write_button = tkinter.Button(self.bottom_frame, text='Write',command=self.write)
        self.Read_button.pack(side = 'left')
        self.Write_button.pack(side = 'left')

        self.top_frame.pack()
        self.filecontent_frame.pack()
        self.fileaddress_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def read(self): #在文本框显示读出的文件内容
        text =''
        File_Address = self.Address_Entry.get()
        with open(File_Address,'r') as file:
            text=file.read()
        self.BytesVar.set(str(len(text)))
        self.Content_text.delete(0.0,tkinter.END)
        self.Content_text.insert('insert',text)

    def write(self): #在文本框要写入的文件内容
        text=self.Content_text.get(0.0,tkinter.END)
        File_Address = self.Address_Entry.get()
        with open(File_Address,'w') as file:
            file.write(text)
        self.BytesVar.set(str(len(text)))
            
gui = MyGUI()