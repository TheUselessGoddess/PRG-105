"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter
import tkinter.messagebox

# TODO 13.2 Using the tkinter Module
print("=" * 10, "Section 13.2 using tkinter", "=" * 10)
# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter. Use the class name MyGUI2
class MyGUI2:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text= 'Nick T')
        self.label.pack()
        tkinter.mainloop()
my_gui = MyGUI2()
# TODO 13.3 Adding a label widget
print("=" * 10, "Section 13.3 adding a label widget", "=" * 10)
# Add a label to MyGUI2 (above) that prints your first and last name; pack the label
# Create an instance of MyGUI2

# TODO 13.4 Organizing Widgets with Frames
print("=" * 10, "Section 13.4 using frames", "=" * 10)
# Create a MyGUI3 class that creates a window with two frames
# In the top Frame add labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester
# Create an instance of MyGUI3
class MyGUI3:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.label_top = tkinter.Label(self.main_window, text= 'Name: Nick T, Major: Game Design/Programming')
        self.label_bottom = tkinter.Label(self.bottom_frame, text= 'PROGRAMMING LOGIC PRG-105-001L')
        self.label_top.pack(side = 'top')
        self.label_bottom.pack(side = 'left')
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

gui2 = MyGUI3()
# TODO 13.5 Button Widgets and info Dialog Boxes
print("=" * 10, "Section 13.5 button widgets and info dialogs", "=" * 10)
# Create a GUI that will tell a joke
# Use a button to show the punch line, which should appear in a dialog box
# Create an instance of the GUI
class JokeGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.my_button = tkinter.Button(self.main_window, text = "Why couldn't the pony sing a lullaby?", command = self.do_something)
        self.my_button.pack()
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'She was a little horse.')

gui_joke = JokeGUI()
# TODO 13.6 getting input / 13.7 Using Labels as output fields
print("=" * 10, "Section 13.6-13.7 input and output using Entry and Label", "=" * 10)
# Using the program in 13.10 kilo converter as a sample,
# create a program to convert inches to centimeters
class Converter:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        #Top Frame Things
        self.prompt_label = tkinter.Label(self.top_frame, text = 'Enter a distance in inches: ')
        self.value_entry = tkinter.Entry(self.top_frame, width = 10)
        #Bottom Frame Things
        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Convert', command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)
        #Packing
        self.prompt_label.pack(side = 'left')
        self.value_entry.pack(side = 'left')
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        self.top_frame.pack()
        self.bottom_frame.pack()
        #Loop Entry
        tkinter.mainloop()

    def convert(self):
        inch = float(self.value_entry.get())
        centimeters = 2.54 * inch
        tkinter.messagebox.showinfo('Results', str(inch) + ' inches is equal to ' + str(centimeters) + ' centimeters.')

inch_convert = Converter()
