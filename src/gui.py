import tkinter

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.button = tkinter.Button(self)
        self.button['text'] = 'Test'
        self.button['command'] = self.get_data
        self.button.pack(side='top')

    def get_data(self):
        pass

m = tkinter.Tk()
app = Application(master=m)
app.mainloop()