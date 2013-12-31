from Tkconstants import NE
import Tkinter
from L07CanvasGridCoord import drawGrid

top = Tkinter.Tk()

frame = Tkinter.Frame(top, width=800, height=800)


def key_press(event):
	print "pressed", repr(event.char)

def left_pressed(event):
	print "left pressed", repr(event.char)

top.bind("a", key_press)
top.bind("<Left>", left_pressed)

# frame.bind("a", key_press)
frame.pack()

canvas = Tkinter.Canvas(frame, height=800, width=800, bg="white")

# canvas.bind("a", key_press)
filename = Tkinter.PhotoImage(file="ball.gif")
image = canvas.create_image(150, 150, anchor=NE, image=filename)

def move_monster(canvas, fx0, fy0):
	fw, fh = 80, 80
	ew, eh = 40, 30

	ex0 = fx0 + 30
	ey0 = fy0 - 20

	canvas.coords(arc, fx0 - fw, fy0 - fh, fx0 + fw, fy0 + fh)
	canvas.coords(oval, ex0, ey0, ex0 + ew, ey0 + eh)

def draw_monster(canvas, fx0, fy0):
	fw, fh = 80, 80
	ew, eh = 40, 30

	ex0 = fx0 + 30
	ey0 = fy0 - 20

	global arc
	arc = canvas.create_arc(fx0 - fw, fy0 - fh, fx0 + fw, fy0 + fh, start=0, extent=270, fill="red")

	global oval
	oval = canvas.create_oval(ex0, ey0, ex0 + ew, ey0 + eh, fill="blue")

draw_monster(canvas, 100, 100)
drawGrid(canvas)

canvas.pack()
top.focus()
top.mainloop()
