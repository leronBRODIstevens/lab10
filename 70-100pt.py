##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget,
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!
square = drawpad.create_rectangle(260,190,560,650, fill='red')
line = drawpad.create_line(260,190,420,0)
line = drawpad.create_line(420,0,560,190)
square = drawpad.create_rectangle(310,230,370,290, fill='green')
square = drawpad.create_rectangle(520,390,580,450, fill='green')
square = drawpad.create_rectangle(520,230,580,290, fill='green')
square = drawpad.create_rectangle(260,190,560,650, fill='green')


root.mainloop()
