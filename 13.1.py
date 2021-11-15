import tkinter
import tkinter.messagebox

class Name_Address:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)
        self.show_info_button = tkinter.Button(self.top_frame, text = 'Show Info', command = self.show_info)
        self.label1 = tkinter.Label(self.top_frame, text = '')

        self.label1.pack()
        self.top_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'bottom')
        self.show_info_button.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def show_info(self):
        self.label1.config(text = 'Nick T\n274 Baily Drive\nWaynseville, NC 27999')

info_shower = Name_Address()

